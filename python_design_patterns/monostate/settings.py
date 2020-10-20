from typing import Any, Dict


class Font():
    _state: Dict[str, Any] = {'size': 12, 'color': 'black'}

    @property
    def size(self) -> int:
        return self._state['size']

    @property
    def color(self) -> str:
        return self._state['color']

    def set_size(self, value: int) -> None:
        self._state['size'] = value

    def set_color(self, value: str) -> None:
        self._state['color'] = value
