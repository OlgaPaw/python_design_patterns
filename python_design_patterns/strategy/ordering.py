from typing import Iterable

from python_design_patterns.strategy.students_view import OrderingStrategy, Student


class IndexOrder(OrderingStrategy):
    @staticmethod
    def sort(students: Iterable[Student]) -> Iterable[Student]:
        return sorted(students, key=lambda s: s.index)


class NotesOrder(OrderingStrategy):
    @staticmethod
    def sort(students: Iterable[Student]) -> Iterable[Student]:
        return sorted(students, key=lambda s: s.note)


class SurnameOrder(OrderingStrategy):
    @staticmethod
    def sort(students: Iterable[Student]) -> Iterable[Student]:
        return sorted(students, key=lambda s: s.surname)
