from reverse_string import reverse_one, reverse_two, reverse_three

def test_reverse_one():
    assert reverse_one

def test_reverse_two():
    assert reverse_two

def test_reverse_three():
    assert reverse_three

def test_reverse_one_reverses_string():
    x = "hello there"
    actual = reverse_one(x)
    expected = "ereht olleh"
    assert actual == expected

def test_reverse_two_reverses_string():
    x = "hello there"
    actual = reverse_two(x)
    expected = "ereht olleh"
    assert actual == expected

def test_reverse_three_reverses_string():
    x = "hello there"
    actual = reverse_three(x)
    expected = "ereht olleh"
    assert actual == expected
