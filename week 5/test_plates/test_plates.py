from plates import is_valid


def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_length():
    assert is_valid("C") == False
    assert is_valid("CS50") == True
    assert is_valid("HELLOCS50") == False

def test_punct():
    assert is_valid("AB-123") == False
    assert is_valid("AB_123") == False

def test_starting_two_letters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
