from insertion_sort import insertion_sort, check_sort
from numpy.random import seed
from numpy.random import randint

def test_insertion_sort():
    assert insertion_sort

def test_check_sort():
    assert check_sort

def test_check_sort_returns_true_with_sorted_arr():
    x = [1,2,3,4,5,6,7,8,9]
    actual = check_sort(x)
    expected = True
    assert actual == expected



def test_check_sort_returns_false_with_unsorted_arr():
    x = [1,2,3,4,5,6,1,7,8]
    actual = check_sort(x)
    expected = False
    assert actual == expected

def test_check_sort_works_negative_numbers():
    x = [1,-2,3,4,5,6,7,8]
    actual = check_sort(x)
    expected = False
    assert actual == expected

def test_insertion_sort_sorts_numbers():
    x = [2,4,5,3,1]
    actual = insertion_sort(x)
    expected = [1,2,3,4,5]
    assert actual == expected

def test_insertion_sort_with_mixed_negative_numbers():
    x = [1,-2,3,-4,5,-6]
    actual = insertion_sort(x)
    expected = [-6,-4,-2,1,3,5]
    assert actual == expected

def test_insertion_sort_with_randomly_generated_list():
    nums = randint(0,100,50)
    x = insertion_sort(nums)
    actual = check_sort(x)
    expected = True
    assert actual == expected


    
