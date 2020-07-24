from python_design_patterns.strategy.display import FullNameDisplay, IndexDisplay
from python_design_patterns.strategy.ordering import IndexOrder, NotesOrder, SurnameOrder
from python_design_patterns.strategy.students_view import Student, StudentsView

STUDENTS = [
    Student(1, "Jan", "Kowalski", 4),
    Student(5, "Janina", "Kowalska", 2),
    Student(10, "Karol", "Adamowicz", 3),
    Student(2, "Adam", "Zieba", 5),
]


def test_index_view_index_order():
    index_view = StudentsView(
        ordering_strategy=IndexOrder(),
        display_strategy=IndexDisplay(),
    )

    report = index_view.get_notes_report(STUDENTS)
    assert report == {
        "1": 4,
        "2": 5,
        "5": 2,
        "10": 3,
    }


def test_index_view_notes_order():
    index_view = StudentsView(
        ordering_strategy=NotesOrder(),
        display_strategy=IndexDisplay(),
    )

    report = index_view.get_notes_report(STUDENTS)
    assert report == {
        "5": 2,
        "10": 3,
        "1": 4,
        "2": 5,
    }


def test_full_name_view_notes_order():
    index_view = StudentsView(
        ordering_strategy=NotesOrder(),
        display_strategy=FullNameDisplay(),
    )

    report = index_view.get_notes_report(STUDENTS)
    assert report == {
        "Kowalska Janina": 2,
        "Adamowicz Karol": 3,
        "Kowalski Jan": 4,
        "Zieba Adam": 5,
    }


def test_full_name_view_surname_order():
    index_view = StudentsView(
        ordering_strategy=SurnameOrder(),
        display_strategy=FullNameDisplay(),
    )

    report = index_view.get_notes_report(STUDENTS)
    assert report == {
        "Adamowicz Karol": 3,
        "Kowalska Janina": 2,
        "Kowalski Jan": 4,
        "Zieba Adam": 5,
    }
