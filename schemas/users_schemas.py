from pydantic import EmailStr, BaseModel, Field


class UserBase(BaseModel):
    """Базовая схема пользователя"""
    username: str = Field(description='Username пользователя')
    name: str = Field(description='Имя пользователя')


class UserEmail(UserBase):
    """Схема пользователя с email"""
    email: EmailStr = Field(description='Email пользователя')


class UserFull(UserEmail):
    """Полная схема пользователя"""
    id: int = Field(description='id пользователя')


class UserIn(UserEmail):
    """Схема пользователя которая приходит от клиентов"""
    password: str = Field(description='Пароль пользователя')


class UserOut(UserFull):
    """Схема пользователя которая уходит клиентам"""
    ...
