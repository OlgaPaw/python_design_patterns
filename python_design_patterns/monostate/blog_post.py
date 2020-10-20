from abc import ABCMeta
from typing import List

from .settings import Font


class TextField(metaclass=ABCMeta):
    def __init__(self, text: str):
        self.font = Font()
        self.text = text

    @property
    def font_size(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        return f"<p style='color: {self.font.color}; font-size: {self.font_size}'>{self.text}</p>"


class Title(TextField):
    @property
    def font_size(self) -> int:
        return self.font.size + 5


class Header(TextField):
    @property
    def font_size(self) -> int:
        return self.font.size + 2


class Text(TextField):
    @property
    def font_size(self) -> int:
        return self.font.size


class BlogPost:
    def __init__(self, html_items: List[TextField]):
        self.html = html_items

    def __str__(self) -> str:
        return "<br />".join(str(item) for item in self.html)
