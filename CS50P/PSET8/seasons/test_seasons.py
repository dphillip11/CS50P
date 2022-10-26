from seasons import get_minutes, n2w
import pytest
from datetime import date, timedelta, datetime

def test_n2w1():
    assert n2w(1234) == "One thousand, two hundred thirty-four minutes"
    assert n2w(1234234) == "One million, two hundred thirty-four thousand, two hundred thirty-four minutes"

def test_n2w2():
    with pytest.raises(ValueError):
        n2w(-1)

def test_n2w3():
    with pytest.raises(ValueError):
        n2w("cat")

def test_getmins1():
    yesterday = str((date.today() - timedelta(days=1)))
    assert get_minutes(yesterday) == 24 * 60

def test_getmins2():
    year = str((date.today() - timedelta(days=365)))
    assert get_minutes(year) == 525600

def test_season1():
    year = str((date.today() - timedelta(days=365)))
    assert n2w(get_minutes(year)) == "Five hundred twenty-five thousand, six hundred minutes"