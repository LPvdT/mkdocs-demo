import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Self

class Language(Enum):
    PYTHON: str
    BASH: str

class ITrolling(metaclass=ABCMeta):
    x: Incomplete
    n: Incomplete
    def __init__(self, x: float, n: int) -> None: ...
    @property
    @abc.abstractmethod
    @abstractmethod
    def multiple(self) -> float: ...
    @abstractmethod
    def from_dict(cls, d: dict[str, int]) -> Self: ...
