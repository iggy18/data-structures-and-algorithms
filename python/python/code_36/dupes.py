def doops(string):
    letters = dict()
    for char in string:
        letters[char] = letters.get(char, 0) + 1
    return any([value > 1 for value in letters.values()])
