from fuel import gauge, convert
import pytest

def test_value():
    with pytest.raises(ValueError):
        convert('A/B')
        convert('5/4')

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('0/0')


def test_full():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

def test_format():
    assert gauge(50) == '50%'

def test_correct_conv():
    assert convert('3/4') == 75
