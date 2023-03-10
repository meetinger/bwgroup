from logging.config import dictConfig

from fastapi import FastAPI

from core.settings import settings
from routes import auth_routes, users_routes, transactions_routes

dictConfig(settings.LOGGER_CONFIG)

tags_metadata = [
    {
        "name": "auth",
        "description": "Регистрация и аутентификация"
    },
    {
        "name": "users",
        "description": "Получение пользовательской информации"
    },
    {
        "name": "transactions",
        "description": "Операции с транзакциями"
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.include_router(auth_routes.router)
app.include_router(users_routes.router)
app.include_router(transactions_routes.router)
