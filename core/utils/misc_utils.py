import random
import string
from typing import Type

from pydantic import BaseModel

from db.database import Base


def gen_random_str(str_len: int, symbols: str = string.ascii_letters + string.digits) -> str:
    """Возвращает строку из случайных символов"""
    return ''.join(random.choices(symbols, k=str_len))


def sqlalchemy_to_pydantic_or_dict(pydantic_cls: Type[BaseModel], sqlalchemy_obj: Base,
                                   to_dict: bool = False) -> BaseModel | dict:
    """Преобразование модели SqlAlchemy в модель Pydantic"""
    data_dct = {key: getattr(sqlalchemy_obj, key) for key in pydantic_cls.__fields__.keys()}
    return data_dct if to_dict else pydantic_cls(**data_dct)
