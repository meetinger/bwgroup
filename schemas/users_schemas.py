from decimal import Decimal

from pydantic import EmailStr, BaseModel, Field

from schemas.transactions_schemas import TransactionOut


class UserBase(BaseModel):
    """Базовая схема пользователя"""
    username: str = Field(description='Username пользователя')
    name: str = Field(description='Имя пользователя')



class UserFull(UserBase):
    """Полная схема пользователя"""
    id: int = Field(description='id пользователя')
    balance: Decimal = Field(description='Баланс пользователя')


class UserIn(UserBase):
    """Схема пользователя которая приходит от клиентов"""
    password: str = Field(description='Пароль пользователя')


class UserOut(UserFull):
    """Схема пользователя которая уходит клиентам"""
    ...
    # last_transactions: list[TransactionOut] = Field(description='Последние 5 транзакций')


class Token(BaseModel):
    """Схема токена"""
    access_token: str = Field(description='Access токен')
    refresh_token: str = Field(description='Refresh токен')
    token_type: str = Field(description='Тип токена(Bearer)')


class RefreshTokenIn(BaseModel):
    """Refresh токен"""
    refresh_token: str = Field(description='Refresh токен')
