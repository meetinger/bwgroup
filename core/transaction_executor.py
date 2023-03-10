import asyncio
import concurrent.futures
import logging
import threading
from collections import defaultdict

from sqlalchemy.orm import Session

from db.crud import users_cruds, transactions_cruds
from db.database import get_db_ctx
from db.enums.transactions_enums import TransactionStatus
from db.models import Transaction


logger = logging.getLogger(__name__)

def process_transaction(transaction: Transaction, db: Session):
    """Выполнить транзакцию"""
    logger.debug(msg=f'Executing transaction {transaction.id}...')
    result = None
    try:
        result = users_cruds.change_user_balance_by_delta(user_id=transaction.user_id, delta=transaction.delta,
                                                          db=db)
    except ValueError:
        result = None
    if result is not None:
        logger.debug(msg=f'Executing transaction {transaction.id} successful')
        return transactions_cruds.change_transaction_status(transaction_id=transaction.id,
                                                            status=TransactionStatus.SUCCESSFUL, db=db)
    logger.debug(msg=f'Executing transaction {transaction.id} rejected')
    return transactions_cruds.change_transaction_status(transaction_id=transaction.id,
                                                        status=TransactionStatus.REJECTED, db=db)


def process_users_transactions(transactions: dict):
    """Выполнить транзакции пользователя"""
    with get_db_ctx() as db:
        return [process_transaction(transaction, db=db) for transaction in transactions.values()]


class TransactionExecutor(threading.Thread):
    """Исполнитель транзакций"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, daemon=True)
        self.is_stop = False
        self.transactions_users_queues = defaultdict(dict)  # у каждого пользователя своя очередь запросов в словаре

    def fetch_transactions(self):
        """Получить все транзакции и распределить их по очередям"""
        logger.debug(msg='Fetching transactions...')
        with get_db_ctx() as db:
            fetched = transactions_cruds.get_transactions_by_status(status=TransactionStatus.PENDING, db=db)
            for transaction in fetched:
                self.transactions_users_queues[transaction.user_id][transaction.id] = transaction

    def set_stop(self, val: bool):
        self.is_stop = val

    def add_transaction(self, transaction_db: Transaction):
        """Добавить транзакцию в очередь"""
        logger.debug(msg='Add transaction to Executor')
        self.transactions_users_queues[transaction_db.user_id][transaction_db.id] = transaction_db

    async def _run(self):
        """Корутина потока"""
        while not self.is_stop:
            logger.debug(msg='Transaction Executor iteration...')
            try:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = []
                    for user_id, transactions in self.transactions_users_queues.items():
                        futures.append(executor.submit(process_users_transactions, transactions=transactions))
                    if futures:
                        concurrent.futures.wait(futures)
                self.transactions_users_queues.clear()
            except Exception as e:
                logger.error(msg=f'Transaction Executor error! {e}', exc_info=e)
            await asyncio.sleep(1)

    def run(self) -> None:
        """Запустить Executor"""
        logger.debug(msg=f'Starting Transaction Executor...')
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._run())


transaction_executor = TransactionExecutor()
