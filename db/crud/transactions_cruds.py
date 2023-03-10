from sqlalchemy import desc
from sqlalchemy.orm import Session

from db.models import Transaction, User
from schemas.transactions_schemas import TransactionIn


def create_new_transaction(transaction: TransactionIn, current_user: User, db: Session) -> Transaction:
    """Создание новой транзакции"""
    transaction_db = Transaction(delta=transaction.delta, status=transaction.status, datetime=transaction.datetime, user_id=current_user.id)
    db.add(transaction_db)
    db.commit()
    db.refresh(transaction_db)
    return transaction_db


def get_last_user_transactions(limit: int, current_user: User, db: Session) -> list:
    """Получить последние транзакции текущего пользователя"""
    transactions = db.query(Transaction).filter_by(user_id=current_user.id).order_by(desc(Transaction.datetime)).limit(limit).all()
    return transactions
