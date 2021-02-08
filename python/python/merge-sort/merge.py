def check_sort(arr):
    prev = float('-inf')
    for num in arr:
        if num < prev:
            return False
        if num >= prev:
            prev = num
    return True

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        left_index_position = 0
        right_index_position = 0
        output_arr_position = 0
        while left_index_position <len(left) and right_index_position < len(right):
            if left[left_index_position] < right[right_index_position]:
                arr[output_arr_position] = left[left_index_position]
                left_index_position += 1
            else:
                arr[output_arr_position] = right[right_index_position]
                right_index_position += 1
            output_arr_position += 1
        while left_index_position < len(left):
            arr[output_arr_position] = left[left_index_position]
            left_index_position += 1
            output_arr_position += 1
        while right_index_position < len(right):
            arr[output_arr_position] = right[right_index_position]
            right_index_position += 1
            output_arr_position += 1
        return arr


