from python_design_patterns.command.commands.abstract_command import Command, Number


class Add(Command):
    def __init__(self, value: Number):
        self.value: Number = value

    def execute(self, current: Number) -> Number:
        return current + self.value

    def revoke(self, current: Number) -> Number:
        return current - self.value
