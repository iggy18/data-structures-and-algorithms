def cleaner(string):
    return string.replace(' ', '').lower()

def is_anagram_sort(string_one, string_two):
    first = cleaner(string_one)
    second = cleaner(string_two)
    return sorted(first) == sorted(second)

def is_anagram_dict(string_one, string_two):
    first = cleaner(string_one)
    second = cleaner(string_two)
    check = dict()
    if len(first) != len(second):
        return False
    for char in first:
        check[char] = check.get(char, 0) + 1
    for char in second:
        check[char] = check.get(char, 0) - 1
    for char in check:
        if check[char] != 0:
            return False
    return True
