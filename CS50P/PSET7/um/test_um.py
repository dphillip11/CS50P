from um import count


def test1():
    assert count("I have three, um, four cats") == 1


def test2():
    assert count("I have three yummy cakes") == 0


def test3():
    assert count("Um, I have three, um, yummy cakes and um, 3 cats.") == 3


def test4():
    assert count("That's a nice house") == 0


def test5():
    assert count("That's a nice um") == 1


def test6():
    assert count("That's a nice! Um!") == 1
