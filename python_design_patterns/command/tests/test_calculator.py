import pytest

from python_design_patterns.command.calculator import Calculator
from python_design_patterns.command.commands.abstract_command import Command, Number
from python_design_patterns.command.commands.add import Add
from python_design_patterns.command.commands.exceptions import NoCommandToRevokeException
from python_design_patterns.command.commands.multiply import Multiply


@pytest.fixture(name='calculator')
def calc() -> Calculator:
    return Calculator()


def test_empty_calc(calculator: Calculator) -> None:
    assert calculator.result == 0


def test_add_command(calculator: Calculator) -> None:
    calculator.execute(Add(5))
    assert calculator.result == 5


def test_revoke_add(calculator: Calculator) -> None:
    calculator.execute(Add(5))
    calculator.revoke()
    assert calculator.result == 0


def test_revoke_add_multiple(calculator: Calculator) -> None:
    calculator.execute(Add(5))
    calculator.execute(Add(10))
    calculator.execute(Add(2))

    calculator.revoke()
    calculator.revoke()
    assert calculator.result == 5


def test_cannot_revoke_empty(calculator: Calculator) -> None:
    calculator.execute(Add(5))

    calculator.revoke()

    with pytest.raises(NoCommandToRevokeException):
        calculator.revoke()

    assert calculator.result == 0


def test_multiply_command(calculator: Calculator) -> None:
    calculator.execute(Add(1))
    calculator.execute(Multiply(5))
    assert calculator.result == 5


def test_revoke_multiply(calculator: Calculator) -> None:
    calculator.execute(Add(1))
    calculator.execute(Multiply(5))
    calculator.revoke()
    assert calculator.result == 1


def test_multiply_zero(calculator: Calculator) -> None:
    calculator.execute(Add(1))
    calculator.execute(Multiply(0))
    calculator.revoke()
    assert calculator.result == 1


def test_can_add_other_command(calculator: Calculator) -> None:
    class NoneCommand(Command):
        def execute(self, current: Number) -> Number:
            return current

        revoke = execute

    calculator.execute(NoneCommand())
    assert calculator.result == 0
    calculator.revoke()
    assert calculator.result == 0
