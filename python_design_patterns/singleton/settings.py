from python_design_patterns.singleton.singleton import SingletonMeta


class Font(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._color = 'black'
        self._size = 12

    @property
    def size(self) -> int:
        return self._size

    @property
    def color(self) -> str:
        return self._color

    def set_size(self, value: int) -> None:
        self._size = value

    def set_color(self, value: str) -> None:
        self._color = value
