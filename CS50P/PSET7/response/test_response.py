from response import validate

def test1():
    validate('malan@harvard.edu') == 'Valid'

def test2():
    validate('malan@@@harvard.edu') == 'Invalid'

def test3():
    validate('malan@harvard.edu.edu') == 'Invalid'

def test4():
    validate('malan@harvard..edu') == 'Invalid'