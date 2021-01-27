from sum_matrix import add_matrix

def test_func_adds_list_vlaues():
    x = [[1,2,3], [4,5,6], [7,8,9]]
    actual = add_matrix(x)
    expected = [6, 15, 24]
    assert actual == expected

def test_empty_matrix_returns_zero():
    x = [[]]
    actual = add_matrix(x)
    expected = [0]
    assert actual == expected

def test_func_works_with_negative_mix():
    x = [[-1,2,3], [4,5,-6], [7,-8,9]]
    actual = add_matrix(x)
    expected = [4, 3, 8]
    assert actual == expected


def test_func_works_with_all_negative():
    x = [[-1,-2,-3], [-4,-5,-6], [-7,-8,-9]]
    actual = add_matrix(x)
    expected = [-6, -15, -24]
    assert actual == expected

def test_func_works_with_different_sized_list():
    x = [[1,2,3], [4,5,6], [7,8,9], [10], [11, 12], [13, 14, 15, 16, 17, 18]]
    actual = add_matrix(x)
    expected = [6, 15, 24, 10, 23, 93]
    assert actual == expected
