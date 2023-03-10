import asyncio
import concurrent.futures
import threading
from collections import defaultdict

from sqlalchemy.orm import Session

from db.crud import users_cruds, transactions_cruds
from db.database import get_db_ctx
from db.enums.transactions_enums import TransactionStatus
from db.models import Transaction


def process_transaction(transaction: Transaction, db: Session):
    """Выполнить транзакцию"""
    result = None
    try:
        result = users_cruds.change_user_balance_by_delta(user_id=transaction.user_id, delta=transaction.delta,
                                                          db=db)
    except ValueError:
        result = None
    if result is not None:
        return transactions_cruds.change_transaction_status(transaction_id=transaction.id,
                                                            status=TransactionStatus.SUCCESSFUL, db=db)
    return transactions_cruds.change_transaction_status(transaction_id=transaction.id,
                                                        status=TransactionStatus.REJECTED, db=db)


def process_users_transactions(transactions: dict):
    with get_db_ctx() as db:
        return [process_transaction(transaction, db=db) for transaction in transactions.values()]


class TransactionExecutor(threading.Thread):
    """Исполнитель транзакций"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, daemon=True)
        self.is_stop = False
        self.transactions_user_buf = defaultdict(dict)

    def fetch_transactions(self):
        with get_db_ctx() as db:
            fetched = transactions_cruds.get_transactions_by_status(status=TransactionStatus.PENDING, db=db)
            for transaction in fetched:
                self.transactions_user_buf[transaction.user_id][transaction.id] = transaction

    def set_stop(self, val: bool):
        self.is_stop = val

    def add_transaction(self, transaction_db: Transaction):
        self.transactions_user_buf[transaction_db.user_id][transaction_db.id] = transaction_db

    async def _run(self):
        while not self.is_stop:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = []
                for user_id, transactions in self.transactions_user_buf.items():
                    futures.append(executor.submit(process_users_transactions, transactions=transactions))
                for future in concurrent.futures.as_completed(futures):
                    pass
            self.transactions_user_buf.clear()
            await asyncio.sleep(1)

    def run(self) -> None:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._run())


transaction_executor = TransactionExecutor()
