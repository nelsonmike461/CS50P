from bank import value

def test_value():
    assert value("hello ") == 0
    assert value("HELLO ") == 0
    assert value("hi yo") == 20
    assert value("HI YO") == 20
    assert value("yoyoyo") == 100
    assert value("YOYOYO") == 100




