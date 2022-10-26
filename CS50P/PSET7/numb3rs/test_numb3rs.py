from numb3rs import validate


def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True


def test_invalid():
    assert validate("3.6.28") == False
    assert validate("3.6.28.255.1") == False


def test_range():
    assert validate("275.3.6.28") == False
    assert validate("255.256.1.1") == False


def test_dots():
    assert validate("...") == False
    assert validate("255.1.1.1.") == False
    assert validate("255111") == False


def test_chars():
    assert validate("a.b.c.d.") == False
    assert validate("1234.1234.1234.1234") == False
