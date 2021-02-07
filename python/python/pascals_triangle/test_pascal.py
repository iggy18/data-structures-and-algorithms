from pascal import pascal_triangle

def test_pascal_triangle():
    assert pascal_triangle

def test_pascal_triangle_returns():
    actual = pascal_triangle(6)
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
    assert actual == expected


def test_pascal_triangle_returns_one():
    actual = pascal_triangle(0)
    expected = [[1]]
    assert actual == expected

def test_pascal_triangle_returns_one_one():
    actual = pascal_triangle(1)
    expected = [[1], [1,1]]
    assert actual == expected

def test_pascal_triangle_returns_one_two_one():
    actual = pascal_triangle(2)
    expected = [[1], [1,1], [1,2,1]]
    assert actual == expected
