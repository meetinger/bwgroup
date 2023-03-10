from decimal import Decimal
from sqlalchemy.orm import Session

from core.security import PasswordUtils
from db.models.users_models import User
from schemas.users_schemas import UserIn


def create_new_user(user: UserIn, db: Session):
    """Создание пользователя"""
    user_db = User(username=user.username,
                   name=user.name,
                   hashed_password=PasswordUtils.hash_password(user.password),
                   balance=Decimal("0")
                   )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def get_user_by_username(username: str, db: Session) -> User | None:
    """Получить пользователя по юзернейму"""
    return db.query(User).filter_by(username=username).first()


def get_user_by_id(user_id, db: Session) -> User | None:
    """Получить пользователя по id"""
    user_db = db.query(User).filter_by(id=user_id).first()
    return user_db


def update_user_balance(user_id: int, balance: Decimal, db: Session) -> Decimal | None:
    """Обновить баланс пользователя"""
    user_db = get_user_by_id(user_id=user_id, db=db)
    if user_db is None:
        return None
    user_db.balance = balance
    db.commit()
    return balance


def change_user_balance_by_delta(user_id: int, delta: Decimal, db: Session) -> Decimal | None:
    """Изменить баланс пользователя на заданную величину"""
    user_db = get_user_by_id(user_id=user_id, db=db)
    if user_db is None:
        return None
    if user_db.balance + delta < 0:
        raise ValueError('Balance less than zero')
    user_db.balance = user_db.balance + delta
    db.commit()
    return user_db.balance


def get_all_users(db: Session) -> list:
    return db.query(User).all()

