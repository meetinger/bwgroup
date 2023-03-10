from sqlalchemy import Column, String, BigInteger, Numeric, Enum
from sqlalchemy.orm import relationship

from db.database import Base
from db.enums.transactions_enums import TransactionsStatus


class Transaction(Base):
    """Класс транзакции"""
    __tablename__ = 'transactions'

    id = Column(BigInteger, primary_key=True, index=True)
    delta = Column(Numeric)
    status = Column(Enum(TransactionsStatus), default=TransactionsStatus.PENDING)

    user_id = Column(BigInteger, index=True)

    user = relationship('User', back_populates='users_transactions')
