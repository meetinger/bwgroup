from decimal import Decimal

from pydantic import BaseModel, Field

class TransactionOut(BaseModel):
    """Схема транзакции"""
    id: int = Field(description='id транзакции')
    user_id: int = Field(description='id пользователя')
    delta: Decimal = Field(description='Изменение баланса')
    status: str = Field(description='Статус транзакции')

