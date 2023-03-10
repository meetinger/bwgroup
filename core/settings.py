# settings

from os import environ
from dotenv import load_dotenv
from core.logger_config import LOGGER_CONFIG as LOGGER_CFG

load_dotenv()


class Settings:

    # DB Setup
    DB_USER: str = environ['DB_USER']
    DB_PASSWORD: str = environ['DB_PASSWORD']
    DB_SERVER: str = environ['DB_SERVER']
    DB_PORT: str = environ['DB_PORT']
    DB_NAME: str = environ['DB_NAME']
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

    # JWT Config
    SECRET_KEY: str = environ['SECRET_KEY']
    ALGORITHM: str = environ['ALGORITHM']
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(environ['ACCESS_TOKEN_EXPIRE_MINUTES'])
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(environ['REFRESH_TOKEN_EXPIRE_MINUTES'])

    # Logger Config
    LOGGER_CONFIG: dict = LOGGER_CFG


settings = Settings()
