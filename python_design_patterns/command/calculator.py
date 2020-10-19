from typing import List

from python_design_patterns.command.commands.abstract_command import Command, Number
from python_design_patterns.command.commands.exceptions import NoCommandToRevokeException


class Calculator:
    def __init__(self) -> None:
        self.result: Number = 0
        self.commands: List[Command] = []

    def execute(self, command: Command) -> None:
        self.result = command.execute(self.result)
        self.commands.append(command)

    def revoke(self) -> None:
        try:
            last_command = self.commands.pop()
        except IndexError as err:
            raise NoCommandToRevokeException() from err
        self.result = last_command.revoke(self.result)
