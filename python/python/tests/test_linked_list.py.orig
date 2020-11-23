import pytest

from linked_list.linked import Node, LinkedList

def test_import():
    assert LinkedList()

def test_can_successfully_instantiate_empty_linked_list():
    nothing = LinkedList()
    assert nothing.head == None


def test_can_properly_insert_into_linked_list():
    list_item = LinkedList()
    list_item.insert("skadoosh")
    assert list_item.head.data == "skadoosh"



def test_Head_properly_points_to_fist_node():
    list_test = LinkedList()
    list_test.insert("electric")
    list_test.insert("ave")
    list_test.insert("new")
    assert list_test.head.data == ("new")


def test_can_properly_insert_multiple_nodes():
    test_list = LinkedList()
    test_list.insert("1")
    test_list.insert("2")
    test_list.insert("3")
    assert test_list.head.next.data == 2

def test_return_true_when_finding_a_value_that_exists():
    test_search = LinkedList()
    test_search.insert("knock")
    test_search.insert("kick")
    test_search.insert("yell")
    assert test_search.includes("kick")


def test_return_false_when_searching_for_value_that_does_not_exsist():
    test_list = LinkedList()
    test_list.insert("whoa")
    test_list.insert("man")
    test_list.insert("youre")
    test_list.insert("on")
    test_list.insert("tv")
    assert not test_list.includes("- that one guy")


def test_can_properly_return_collection_of_all_values_in_list():
    phrase = LinkedList()
    phrase.insert("a")
    phrase.insert("b")
    phrase.insert("c")
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert expected == phrase.__str__()
