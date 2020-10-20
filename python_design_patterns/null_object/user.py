import logging
from abc import ABCMeta


class BaseAddress(metaclass=ABCMeta):
    def __init__(self, address: str = None) -> None:
        self.address = address

    def is_null(self) -> bool:
        raise NotImplementedError

    def send_crow(self) -> None:
        raise NotImplementedError


class Home(BaseAddress):
    def is_null(self) -> bool:
        return False

    def send_crow(self) -> None:
        logging.info("Crow sent to : %s", self.address)


class NullHome(BaseAddress):
    def is_null(self) -> bool:
        return True

    def send_crow(self) -> None:
        pass


class User:
    def __init__(self, first_name: str, last_name: str, address: str = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.home = Home(address) if address else NullHome()

    def send_crow_to_home(self) -> None:
        self.home.send_crow()

    def is_homeless(self) -> bool:
        return self.home.is_null()
