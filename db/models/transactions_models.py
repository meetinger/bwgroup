import datetime as dt
from sqlalchemy import Column, BigInteger, Numeric, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base
from db.enums.transactions_enums import TransactionStatus


class Transaction(Base):
    """Класс транзакции"""
    __tablename__ = 'transactions'

    id = Column(BigInteger, primary_key=True, index=True)
    delta = Column(Numeric)
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING)
    datetime = Column(DateTime, default=dt.datetime.utcnow, index=True)

    user_id = Column(BigInteger, ForeignKey('users.id'), index=True)

    user = relationship('User', back_populates='users_transactions')
