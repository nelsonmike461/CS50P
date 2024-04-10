from numb3rs import validate


def test_validate():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.256") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False

