from linked import Node, LinkedList

def test_node():
    assert Node

def test_linked_list():
    assert LinkedList

def test_empty_list():
    assert LinkedList()

def test_insert_single_node():
    x = LinkedList()
    x.insert("a")
    actual = x.head.val
    expected =  "a"
    assert actual == expected

def test_insert_multiple_node():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.contains()
    expected =  ["e", "d", "c", "b", "a"]
    assert actual == expected

def test_head_node_fist_in_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.head.val
    expected =  "e"
    assert actual == expected

def test_return_true_if_value_in_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.includes("c")
    expected =  True
    assert actual == expected

def test_return_false_if_value_in_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    actual = x.includes("z")
    expected =  False
    assert actual == expected

def test_can_return_all_elements_in_list():
    x = LinkedList()
    x.insert("c")
    x.insert("b")
    x.insert("a")
    actual = x.__str__()
    expected =  "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected
