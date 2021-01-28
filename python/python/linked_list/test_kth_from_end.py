import pytest
from linked import Node, LinkedList

def test_node():
    assert Node

def test_linked_list():
    assert LinkedList

def test_kth_from_end_returns_correct_node_value():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.kth_from_end(2)
    expected =  "c"
    assert actual == expected

def test_where_k_is_greater_than_the_length_of_the_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.kth_from_end(7)
    expected =  "k is greater than length of linked list"
    assert actual == expected


def test_where_k_and_the_length_of_the_list_are_the_same():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.kth_from_end(5)
    expected =  "k is greater than length of linked list"
    assert actual == expected

def test_where_k_is_not_a_positive_integer():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.kth_from_end(-3)
    expected =  "you must enter a positive value"
    assert actual == expected

def test_where_the_linked_list_is_of_a_size_1():
    x = LinkedList()
    x.insert("a")
    actual = x.kth_from_end(0)
    expected =  "a"
    assert actual == expected
