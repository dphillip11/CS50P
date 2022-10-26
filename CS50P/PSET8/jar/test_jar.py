from jar import Jar
import pytest


def test_init():

    jar = Jar()
    assert jar.capacity == 12 and jar.size == 0

    jar2 = Jar(15)
    assert jar2.capacity == 15 and jar.size == 0

    with pytest.raises(ValueError):
        jar3 = Jar("a")

    with pytest.raises(ValueError):
        jar4 = Jar(-1)

    with pytest.raises(ValueError):
        jar5 = Jar(0.5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(5)
    with pytest.raises(ValueError):
        jar.deposit("A")


def test_withdraw():
    jar = Jar(20)
    jar.deposit(20)
    jar.withdraw(5)
    assert jar.size == 15
    jar.withdraw(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.withdraw(15)
    with pytest.raises(ValueError):
        jar.withdraw("A")
