from bank import value

def test_blank():
    assert value('')== 100

def test_hello():
    assert value('hello')== 0

def test_HELLO():
    assert value('HELLO')== 0

def test_hello_string():
    assert value('hello frank')== 0

def test_h():
    assert value('hi')== 20

def test_caps():
    assert value('HI')== 20

def test_not_h():
    assert value('gooseberries')== 100




