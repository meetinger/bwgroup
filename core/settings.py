# settings

from os import environ
from dotenv import load_dotenv
from logger_config import LOGGER_CONFIG as LOGGER_CFG

load_dotenv()


class Settings:
    # Secret Key
    SECRET_KEY: str = environ['SECRET_TOKEN']

    # DB Setup
    DB_USER: str = environ['DB_USER']
    DB_PASSWORD: str = environ['DB_PASSWORD']
    DB_SERVER: str = environ['DB_SERVER']
    DB_PORT: str = environ['DB_PORT']
    DB_NAME: str = environ['DB_NAME']
    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"

    # Logger Config
    LOGGER_CONFIG = LOGGER_CFG


settings = Settings()
