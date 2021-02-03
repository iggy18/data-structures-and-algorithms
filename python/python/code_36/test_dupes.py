from dupes import doops

def test_doops():
    assert doops

def test_dupes_returns_FALSE_if_no_dupes():
    x = "abcdef"
    actual = doops(x)
    expected = False
    assert actual == expected

def test_doops_returns_TRUE_if_dupes():
    x = "abcda"
    actual = doops(x)
    expected = True
    assert actual == expected
