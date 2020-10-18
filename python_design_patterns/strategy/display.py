from typing import Dict, Iterable

from python_design_patterns.strategy.students_view import DisplayStrategy, Student


class IndexDisplay(DisplayStrategy):
    @staticmethod
    def view(students: Iterable[Student]) -> Dict[str, int]:
        return {str(student.index): student.note for student in students}


class FullNameDisplay(DisplayStrategy):
    @staticmethod
    def view(students: Iterable[Student]) -> Dict[str, int]:
        return {f'{student.surname} {student.name}': student.note for student in students}
