from abc import ABCMeta, abstractmethod
from typing import Union

Number = Union[int, float]


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, current: Number) -> Number:
        raise NotImplementedError

    @abstractmethod
    def revoke(self, current: Number) -> Number:
        raise NotImplementedError