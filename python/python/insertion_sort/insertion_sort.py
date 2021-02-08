def check_sort(arr):
    prev = float('-inf')
    for num in arr:
        if num < prev:
            return False
        if num >= prev:
            prev = num
    return True

def insertion_sort(arr):
    pass



