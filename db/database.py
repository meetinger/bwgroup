from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session, Session

from core.settings import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

ScopedSession = scoped_session(SessionLocal)

Base = declarative_base()


def get_db() -> Generator:
    """Функция для получения объекта сессии БД, удобно юзать для тестирования"""
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@contextmanager
def get_db_ctx() -> Session:
    db = None
    try:
        db = ScopedSession()
        yield db
    finally:
        return None
