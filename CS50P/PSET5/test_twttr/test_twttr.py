from twttr import shorten

def test_lwr():
    assert shorten('cheese') == 'chs'

def test_upr():
    assert shorten('CHEESE') == 'CHS'

def test_sentence():
    assert shorten('this IS a caT') == 'ths S  cT'

def test_numbers():
    assert shorten('l1ft') == 'l1ft'

def test_punct():
    assert shorten('l!aft') == 'l!ft'