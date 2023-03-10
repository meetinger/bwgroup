import datetime as dt
from typing import Optional
from decimal import Decimal

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from core.utils.misc_utils import sqlalchemy_to_pydantic_or_dict
from db.crud import transactions_cruds
from db.database import get_db
from db.enums.transactions_enums import TransactionStatus
from db.models import User
from routes.auth_routes import get_current_user_from_token
from routes.docs_examples import transactions_routes_examples
from schemas.docs_examples import transactions_schemas_examples
from schemas.transactions_schemas import TransactionOut, TransactionIn, TransactionDelta

router = APIRouter(prefix="/transactions", tags=['transactions'])


@router.get('/', response_model=list[TransactionOut],
            responses=transactions_routes_examples.current_user_transactions_list)
async def current_user_transactions_list(limit: Optional[int] = 5,
                                         current_user: User = Depends(get_current_user_from_token),
                                         db: Session = Depends(get_db)):
    """Получение информации о текущем пользователе"""
    transactions_db = transactions_cruds.get_last_user_transactions(limit=limit, current_user=current_user, db=db)
    return [sqlalchemy_to_pydantic_or_dict(TransactionOut, transaction) for transaction in transactions_db]


@router.post('/create_transaction', response_model=TransactionOut, responses=transactions_routes_examples.create_transaction)
async def create_transaction(transaction_delta: TransactionDelta = Body(examples=transactions_schemas_examples.transaction_delta_examples),
                                         current_user: User = Depends(get_current_user_from_token),
                                         db: Session = Depends(get_db)):
    """
    Создание транзакции
    """
    transaction_in = TransactionIn(delta=Decimal(transaction_delta.delta), datetime=dt.datetime.utcnow(), status=TransactionStatus.PENDING,
                                   user_id=current_user.id)
    transaction_db = transactions_cruds.create_new_transaction(transaction=transaction_in, current_user=current_user, db=db)
    return sqlalchemy_to_pydantic_or_dict(TransactionOut, transaction_db)
