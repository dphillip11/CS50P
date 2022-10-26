from working import convert
import pytest


def test1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test4():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test5():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test6():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test7():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test8():
    with pytest.raises(ValueError):
        convert("09:00 AM to 25:60 PM")


def test9():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
