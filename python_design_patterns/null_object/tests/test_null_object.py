import logging

from ..user import User

JON_SNOW = User('John', 'Snow', 'The Wall')
HOMELESS = User('Home', 'Less')
USERS = [JON_SNOW, HOMELESS]


def test_is_null():
    assert not JON_SNOW.is_homeless()
    assert HOMELESS.is_homeless()


def test_can_run_method_on_null_object(caplog):
    with caplog.at_level(logging.INFO):
        for user in USERS:
            user.send_crow_to_home()

    assert caplog.record_tuples == [('root', logging.INFO, 'Crow sent to : The Wall')]
