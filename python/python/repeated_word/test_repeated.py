from repeated_word import strip_down, not_split, seen_word, which_word_is_repeated_first


def test_strip_down():
    assert strip_down

def test_not_split():
    assert not_split

def test_seen_word():
    assert seen_word

def test_which_word_is_repeated_first():
    assert which_word_is_repeated_first


def test_strip_down_removes_special_chars():
    x = "here, is! some... $tuff"
    actual = strip_down(x)
    expected = "here is some tuff"
    assert actual == expected

def test_not_split_creates_array_from_input():
    x = "here is some stuff"
    actual = not_split(x)
    expected = ["here", "is", "some", "stuff"]
    assert actual == expected

def test_seen_word_returns_repeated_word():
    x = "here is some some stuff"
    y = not_split(x)
    actual = seen_word(y)
    expected = "some"
    assert actual == expected

def test_which_word_is_repeated_first_returns_repeated_words_from_lengthy_input():
    x = 'Once upon a time, there was a brave princess who... '
    actual = which_word_is_repeated_first(x)
    expected = "a"
    assert actual == expected

def test_which_word_is_repeated_first_returns_repeated_words_from_lengthy_input_two():
    x = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    actual = which_word_is_repeated_first(x)
    expected = "it"
    assert actual == expected

def test_which_word_is_repeated_first_returns_repeated_words_from_lengthy_input_three():
    x = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    actual = which_word_is_repeated_first(x)
    expected = "summer"
    assert actual == expected

