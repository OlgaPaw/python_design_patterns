import logging

import pytest

from python_design_patterns.mediator.account import BankAccount, InsufficientBalance
from python_design_patterns.mediator.account_interfaces import WebAccountInterface, ATMAccountInterface


def test_mediator():
    account = BankAccount(balance=100)
    atm_interface = ATMAccountInterface(account)

    assert account.default_mobile_interface.get_balance() == 100
    assert atm_interface.get_balance() == 100


def test_withdraw_notified_on_mobile(caplog):
    account = BankAccount(balance=100)
    atm_interface = ATMAccountInterface(account)

    with caplog.at_level(logging.INFO):
        atm_interface.withdraw(100)
    assert account.default_mobile_interface.get_balance() == 0
    assert account.default_mobile_interface.last_notification == 'Operation on your account succeed: withdraw 100'


def test_cannot_withdraw_when_not_enough_balance():
    account = BankAccount(balance=100)
    atm_interface = ATMAccountInterface(account)

    with pytest.raises(InsufficientBalance):
        atm_interface.withdraw(101)

    assert account.default_mobile_interface.last_notification == 'Operation on your account failed: withdraw 101'


def test_transfer():
    account_from = BankAccount(balance=100)
    account_to = BankAccount(balance=20)
    web_interface = WebAccountInterface(account_from)

    web_interface.transfer(account_to, 50)
    assert web_interface.get_balance() == 50
    assert account_to.balance() == 70

    assert account_from.default_mobile_interface.last_notification == 'Operation on your account succeed: transfer 50'
    assert account_to.default_mobile_interface.last_notification == 'Operation on your account succeed: receive 50'


def test_cannot_transfer_when_not_enough_balance():
    account_from = BankAccount(balance=100)
    account_to = BankAccount(balance=20)
    web_interface = WebAccountInterface(account_from)

    with pytest.raises(InsufficientBalance):
        web_interface.transfer(account_to, 120)

    assert web_interface.get_balance() == 100
    assert account_to.balance() == 20

    assert account_from.default_mobile_interface.last_notification == 'Operation on your account failed: transfer 120'
    assert account_to.default_mobile_interface.last_notification is None
