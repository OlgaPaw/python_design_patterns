from abc import ABCMeta
from dataclasses import dataclass
from typing import Dict, Iterable

# Interface Definition


@dataclass
class Student:
    index: int
    name: str
    surname: str
    note: int


class OrderingStrategy(metaclass=ABCMeta):
    @staticmethod
    def sort(students: Iterable[Student]) -> Iterable[Student]:
        raise NotImplementedError


class DisplayStrategy(metaclass=ABCMeta):
    @staticmethod
    def view(students: Iterable[Student]) -> Dict[str, int]:
        raise NotImplementedError


# Domain Logic


class StudentsView:
    def __init__(
        self,
        ordering_strategy: OrderingStrategy,
        display_strategy: DisplayStrategy,
    ) -> None:
        self.ordering_strategy = ordering_strategy
        self.display_strategy = display_strategy

    def _get_sorted_items(
        self,
        students: Iterable[Student],
    ) -> Iterable[Student]:
        return self.ordering_strategy.sort(students)

    def _get_display(self, students: Iterable[Student]) -> Dict[str, int]:
        return self.display_strategy.view(students)

    def get_notes_report(self, students: Iterable[Student]) -> Dict[str, int]:
        return self._get_display(self._get_sorted_items(students))
