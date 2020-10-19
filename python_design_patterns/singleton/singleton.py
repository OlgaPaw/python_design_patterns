from typing import Any


class SingletonMeta(type):
    _instance: Any = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if not cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance
