import enum


class EnumChoicesMixin:
    """Примесь для enum, которая добавляет методы для получения names, values и (names, values)"""
    @classmethod
    def names(cls: type[enum.Enum], exclude: tuple[enum.Enum] = ()) -> tuple:
        return tuple(i.name for i in cls if i not in exclude)

    @classmethod
    def values(cls: type[enum.Enum], exclude: tuple[enum.Enum] = ()) -> tuple:
        return tuple(i.value for i in cls if i not in exclude)

    @classmethod
    def choices(cls: type[enum.Enum], exclude: tuple[enum.Enum] = ()) -> tuple:
        return tuple((i.name, i.value) for i in cls if i not in exclude)
