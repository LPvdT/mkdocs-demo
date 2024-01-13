"""This module contains interfaces and custom types."""

from abc import (
    ABCMeta,
    abstractmethod,
    abstractproperty,
)
from enum import Enum
from typing import Self


class Language(Enum):
    """
    Enum that represents different programming languages.
    """

    PYTHON: str = "*.py"
    """Python language."""

    BASH: str = "*.sh"
    """Bash language."""


class ITrolling(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, x: float, n: int) -> None:
        pass

    @abstractproperty
    def multiple(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @classmethod
    def from_dict(cls, d: dict[str, int]) -> Self:
        required = ("x", "n")
        obj = {k: v for k, v in d.items()}

        assert obj.keys() in required

        return cls(**obj)
