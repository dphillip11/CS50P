from watch import parse

HTML1 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
HTML2 = (
    '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
)


def test1():
    assert parse(HTML1) == "https://youtu.be/xvFZjo5PgG0"


def test2():
    assert parse(HTML2) == None
