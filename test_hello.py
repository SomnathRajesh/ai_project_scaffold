from hello import hello, bye


def test_hello():
    assert "hello" == hello()


def test_bye():
    assert "bye" == bye()
