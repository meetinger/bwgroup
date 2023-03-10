import logging

from fastapi import Depends, APIRouter

from core.utils.misc_utils import sqlalchemy_to_pydantic_or_dict
from db.models import User
from routes.auth_routes import get_current_user_from_token
from routes.docs_examples import users_routes_examples
from schemas.users_schemas import UserOut


router = APIRouter(prefix="/users", tags=['users'])

logger = logging.getLogger(__name__)

@router.get('/info', response_model=UserOut, responses=users_routes_examples.info_current_user_responses_examples)
async def info_current_user(current_user: User = Depends(get_current_user_from_token)):
    """Получение информации о текущем пользователе"""
    logger.info(msg=f'User {current_user.id} get user info')
    return sqlalchemy_to_pydantic_or_dict(UserOut, current_user)
