from um import count

def test_count():
    assert count("um hey um") == 2
    assert count("um") == 1
    assert count("um hey UM") == 2
    assert count("hey um um ") == 2
    assert count("yummy") == 0



