from rotate import rotate

def test_rotate():
    assert rotate

def test_rotate_works_properly():
    x = [[1,2,3], [1,2,3], [1,2,3]]
    actual = rotate(x)
    expected = [[1,1,1], [2,2,2], [3,3,3,]]
    assert actual == expected
