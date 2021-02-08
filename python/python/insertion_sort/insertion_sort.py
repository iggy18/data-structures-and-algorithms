def check_sort(arr):
    prev = float('-inf')
    for num in arr:
        if num < prev:
            return False
        if num >= prev:
            prev = num
    return True

def insertion_sort(arr):
    for index_num in range(1,len(arr)):
        current_value = arr[index_num]
        current_position = index_num
        while current_position > 0 and arr[current_position-1] > current_value:
            arr[current_position] = arr[current_position-1]
            current_position = current_position - 1
        arr[current_position] = current_value
    return arr


