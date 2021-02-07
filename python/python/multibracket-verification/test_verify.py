from verify import validate

def test_validate():
    assert validate

def test_validate_returns_True_with_an_easy_one():
    x = '[]'
    actual = validate(x)
    expected = True
    assert actual == expected

def test_valid_paren():
    x = '()'
    actual = validate(x)
    expected = True
    assert actual == expected

def test_valid_curly():
    x = '{}'
    actual = validate(x)
    expected = True
    assert actual == expected

def test_non_bal_returns_false():
    x = '[}]'
    actual = validate(x)
    expected = False
    assert actual == expected

def test_with_text():
    x = '[(hello)]'
    actual = validate(x)
    expected = True
    assert actual == expected

def test_false_with_text():
    x = '[{9tails}]}'
    actual = validate(x)
    expected = False
    assert actual == expected

def tests_hard_one():
    x = '{}{Code}[Fellows](())'
    actual = validate(x)
    expected = True
    assert actual == expected




