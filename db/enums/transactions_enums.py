import enum

from core.utils.class_utils import EnumChoicesMixin


class TransactionsStatus(enum.StrEnum, EnumChoicesMixin):
    """Статусы транзакций"""
    PENDING = enum.auto()
    SUCCESSFUL = enum.auto()
    REJECTED = enum.auto()
