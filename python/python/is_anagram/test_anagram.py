from is_anagram import is_anagram_sort, is_anagram_dict, cleaner

def test_cleaner():
    assert cleaner

def test_is_anagram_sort():
    assert is_anagram_sort

def test_is_anagram_dict():
    assert is_anagram_dict

def test_cleaner_removes_spaces():
    x = "h e l l o"
    actual = cleaner(x)
    expected = "hello"
    assert actual == expected

def test_cleaner_makes_lower_case():
    x = "H E L L O"
    actual = cleaner(x)
    expected = "hello"
    assert actual == expected

def test_is_anagram_sort_returns_true_for_anagram():
    x = 'melon'
    y = 'lemon'
    actual = is_anagram_sort(x, y)
    expected = True
    assert actual == expected

def test_is_anagram_sort_returns_false_for_no_anagram():
    x = "whatchyamacallit"
    y = "not a chance"
    actual = is_anagram_sort(x, y)
    expected = False
    assert actual == expected

def test_is_anagram_dict_returns_true_for_anagram():
    x = 'melon'
    y = 'lemon'
    actual = is_anagram_dict(x, y)
    expected = True
    assert actual == expected

def test_is_anagram_dict_returns_false_for_no_anagram():
    x = "whatchyamacallit"
    y = "not a chance"
    actual = is_anagram_dict(x, y)
    expected = False
    assert actual == expected
