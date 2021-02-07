# test if string has balanced brackets "{[()]}" = True "({[}" False
from stacks import Stack


'''
def validate(string):
    make a stack
    Open val
    close val

    for letter in string:
        if letter in open
            enqueue in stack
        if letter in close:
            stack dequeue
        check if stack is empty:
            if not False
        otherwise true
'''
def validate(string):
    seen = Stack()
    opening = '({['
    closing = ')}]'
    for char in string:
        if char in opening:
            seen.push(char)
        elif char in closing:
            same_place = closing.index(char)
            if seen.is_empty() or seen.pop() != opening[same_place]:
                return False
    if not seen.is_empty():
        return False
    return True



