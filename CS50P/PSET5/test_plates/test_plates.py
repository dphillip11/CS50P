from plates import is_valid

def test_short():
    assert is_valid("A") == False

def test_long():
    assert is_valid("ABAAA22222") == False

def test_numbers():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA02") == False

def test_punct():
    assert is_valid("BB. 22") == False

def test_valid():
    assert is_valid("AAA222") == True

def test_letter_first():
    assert is_valid("123456") == False