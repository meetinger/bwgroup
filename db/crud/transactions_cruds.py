from typing import Type, Any

from sqlalchemy import desc
from sqlalchemy.orm import Session, Query

from db.enums.transactions_enums import TransactionStatus
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


def change_transaction_status(transaction_id: int, status: TransactionStatus, db: Session) -> Transaction | None:
    """Изменить статус транзакции"""
    transaction_db = db.query(Transaction).filter_by(id=transaction_id).first()
    transaction_db.status = status
    db.commit()
    return transaction_db


def get_transactions_by_status(status: TransactionStatus, db: Session) -> list:
    """Получить транзакции с опр. статусом"""
    transactions_db = db.query(Transaction).filter_by(status=status).all()
    return transactions_db
