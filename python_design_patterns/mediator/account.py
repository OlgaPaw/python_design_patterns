from abc import ABCMeta
from typing import Any, List, Optional


class Mediator(metaclass=ABCMeta):
    def notify(self, sender: Any, operation: str, **kwargs: Any) -> Any:
        raise NotImplementedError


class Interface(metaclass=ABCMeta):
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    def get_balance(self) -> int:
        return self.mediator.notify(self, 'balance')


class InsufficientBalance(Exception):
    """
    Raised when no enough balance to perform operation
    """


class MobileAccountInterface(Interface):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.notifications: List[str] = []

    def notification(self, message: str, success: bool = True) -> None:
        status = 'succeed' if success else 'failed'
        self.notifications.append(f'Operation on your account {status}: {message}')

    @property
    def last_notification(self) -> Optional[str]:
        return self.notifications[-1] if self.notifications else None


class BankAccount(Mediator):
    def __init__(self, balance: int = 0):
        self._balance = balance
        self.mobile = MobileAccountInterface(self)

    @property
    def default_mobile_interface(self) -> MobileAccountInterface:
        return self.mobile

    def notify(self, sender: Any, operation: str, **kwargs: Any) -> Any:
        return getattr(self, operation)(**kwargs)

    def balance(self) -> int:
        return self._balance

    def receive(self, value: int) -> None:
        self._balance += value
        self.mobile.notification(f'receive {value}')

    def withdraw(self, value: int) -> None:
        if value > self._balance:
            self.mobile.notification(f'withdraw {value}', success=False)
            raise InsufficientBalance()

        self._balance -= value
        self.mobile.notification(f'withdraw {value}')

    def transfer(self, target: Mediator, value: int) -> None:
        if value > self._balance:
            self.mobile.notification(f'transfer {value}', success=False)
            raise InsufficientBalance()

        self._balance -= value
        target.notify(self, 'receive', value=value)
        self.mobile.notification(f'transfer {value}')
