from ..blog_post import BlogPost, Header, Text, Title
from ..settings import Font


def test_monostate_change_affects_all_usages():
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
