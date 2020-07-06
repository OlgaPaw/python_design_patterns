from python_design_patterns.command.commands.abstract_command import Command, Number


class Multiply(Command):
    def __init__(self, value: Number):
        self.value: Number = value
        self.previous: Number

    def execute(self, current: Number) -> Number:
        self.previous = current
        return current * self.value

    def revoke(self, current: Number) -> Number:
        return self.previous