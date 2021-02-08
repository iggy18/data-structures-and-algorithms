def check_sort(arr):
    prev = float('-inf')
    for num in arr:
        if num < prev:
            return False
        if num >= prev:
            prev = num
    return True

def quick_sort(arr):
    items = len(arr)
    if items < 2:
        return arr
    location = 0
    for i in range(1, items):
        if arr[i] <= arr[0]:
            location += 1
            temp = arr[i]
            arr[i] = arr[location]
            arr[location] = temp
    temp = arr[0]
    arr[0] = arr[location]
    arr[location] = temp
    left = quick_sort(arr[0:location])
    right = quick_sort(arr[location+1:items])
    arr = left + [arr[location]] + right
    return arr


