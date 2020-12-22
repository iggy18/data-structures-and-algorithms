def strip_down(some_text):
    """
    this function strips text of
    """

    some_text = some_text.lower()
    replacement = ''
    for char in some_text:
        if char in ".,!@#$%^&*()_+=<>?`~?/|\\[]{}:;()":
            char = ""
        replacement += char
    return replacement

def not_split(some_text):
    output =[]
    temp = ''
    for word in some_text:
        if word == ' ':
            output.append(temp)
            temp = ''
        else:
            temp += word
    if temp:
        output.append(temp)
    return output

def seen_word(arr):
    seen_words = []
    for item in arr:
        if item in seen_words:
            return item
        else:
            seen_words.append(item)

def which_word_is_repeated_first(input):
    stripped = strip_down(input)
    in_array = not_split(stripped)
    print(seen_word(in_array))

which_word_is_repeated_first('Once upon a time, there was a brave princess who... ')

which_word_is_repeated_first('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only... ')

which_word_is_repeated_first('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')

which_word_is_repeated_first(' to be or not to be ')
