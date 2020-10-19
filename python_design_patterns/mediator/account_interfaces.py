from .account import Interface, Mediator


class ATMAccountInterface(Interface):
    def withdraw(self, value: int) -> None:
        return self.mediator.notify(self, 'withdraw', value=value)


class WebAccountInterface(Interface):
    def transfer(self, target: Mediator, value: int) -> None:
        return self.mediator.notify(self, 'transfer', value=value, target=target)
