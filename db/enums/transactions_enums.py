import enum

from core.utils.class_utils import EnumChoicesMixin


class TransactionStatus(EnumChoicesMixin, enum.Enum):
    """Статусы транзакций"""
    PENDING = 'pending'
    SUCCESSFUL = 'successful'
    REJECTED = 'rejected'
