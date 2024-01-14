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
    """
    Abstract base class for implementing trolling interface.
    """

    def __init__(self, x: float, n: int) -> None:
        """
        The above function is an initializer method for a class that takes in
        two parameters, `x` and `n`, and does not return anything.

        Parameters
        ----------
        `x` : `float`
            The parameter `x` is a float, which means it can hold decimal
            values. It is used to store a numerical value.

        `n` : `int`
            The parameter `n` is an integer that represents the number of
            iterations or steps in a process.
        """
        self.x = x
        self.n = n

    def __str__(self) -> str:
        return f"""x={self.x}, n={self.n}, hence the multiple={self.multiple}"""

    def __repr__(self) -> str:
        return f"""{self.x} * {self.n} = {self.multiple}"""

    @abstractproperty
    @abstractmethod
    def multiple(self) -> float:
        pass

    @abstractmethod
    def from_dict(cls, d: dict[str, int]) -> Self:
        pass
