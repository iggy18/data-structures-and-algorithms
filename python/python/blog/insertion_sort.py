def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for value in indexing_length:
        value_to_sort = list_a[value]

        # while value to the left is > value to sort
        while list_a[value - 1] > value_to_sort and value>0:
            # swap values
            list_a[value], list_a[value -1] = list_a[value -1], list_a[value]
            value = value - 1
    return list_a

test = [51, 11, 3, 66, 58, 49, 76, 9, 23, 20, 70, 69, 69, 26, 57, 12, 32, 57, 66, 36, 73, 16, 6, 82, 65, 25, 83, 15, 48, 68, 39, 71, 74, 76, 82, 0, 15, 7, 96, 49, 59, 7, 15, 5, 84, 51, 28, 20, 98, 94]

test = insertion_sort(test)


