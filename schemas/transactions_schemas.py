import datetime as dt

from decimal import Decimal
from pydantic import BaseModel, Field

from db.enums.transactions_enums import TransactionStatus


class TransactionIn(BaseModel):
    """Входящая схема транзакции"""
    delta: Decimal = Field(description='Изменение баланса')
    datetime: dt.datetime = Field(description='Дата и время транзакции(UTC)')
    status: TransactionStatus = Field(description='Статус транзакции')


class TransactionOut(TransactionIn):
    """Схема транзакции, уходящая клиентам"""
    id: int = Field(description='id транзакции')


class TransactionFull(TransactionOut):
    """Полная схема транзакции"""
    user_id: int = Field(description='id пользователя')

class TransactionDelta(BaseModel):
    """
    Изменение баланса
    Cтроковое представление delta нужно для того, чтобы избежать подобного погрешности с плавающей запятой
    """
    delta: str = Field(description="Изменение баланса")
