from python_design_patterns.singleton.blog_post import BlogPost
from python_design_patterns.singleton.settings import Font

from ..blog_post import Header, Text, Title


def test_only_one_instance_created():
    title = Title('My test book')
    chapter1 = Header('Chapter One: How to implement singleton pattern')
    text = Text('You should probably not need it')

    assert id(title.font) == id(chapter1.font) == id(text.font)


def test_singleton_globally_available():
    title = Title('My test book')
    font = Font()

    assert id(title.font) == id(font)


def test_singleton_change_affects_all_usages():
    title = Title('Title')
    chapter1 = Header('Chapter One')
    text = Text('The end.')

    post = BlogPost([title, chapter1, text])

    assert str(post) == (
        "<p style='color: black; font-size: 17'>Title</p><br />"
        "<p style='color: black; font-size: 14'>Chapter One</p><br />"
        "<p style='color: black; font-size: 12'>The end.</p>"
    )

    Font().set_size(1)
    Font().set_color('red')

    assert str(post) == (
        "<p style='color: red; font-size: 6'>Title</p><br />"
        "<p style='color: red; font-size: 3'>Chapter One</p><br />"
        "<p style='color: red; font-size: 1'>The end.</p>"
    )
