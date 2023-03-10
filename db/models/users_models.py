from sqlalchemy import Column, String, BigInteger, Numeric
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    """Класс пользователя"""
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String, index=True)

    balance = Column(Numeric)
    users_transactions = relationship('Transaction', back_populates='user')
