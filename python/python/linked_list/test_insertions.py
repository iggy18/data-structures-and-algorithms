from linked import Node, LinkedList

def test_node():
    assert Node

def test_linked_list():
    assert LinkedList

def test_can_successfully_add_a_node_to_the_end_of_the_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.append("g")
    actual = x.contains()
    expected = ["e","d","c","b","a","g"]
    assert actual == expected

def test_can_successfully_add_multiple_nodes_to_the_end_of_a_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.append("test one")
    x.append("test two")
    actual = x.contains()
    expected = ["e","d","c","b","a", "test one", "test two"]
    assert actual == expected

def test_can_successfully_insert_a_node_before_a_node_located_i_the_middle_of_a_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.insert_before("c", "test")
    actual = x.contains()
    expected = ["e","d","test","c","b","a"]
    assert actual == expected


def test_can_successfully_insert_a_node_before_the_first_node_of_a_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.insert_before("e", "test")
    actual = x.contains()
    expected = ["test","e","d","c","b","a"]
    assert actual == expected

def test_can_successfully_insert_after_a_node_in_the_middle_of_the_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.insert_after("c", "test")
    actual = x.contains()
    expected = ["e","d","c","test","b","a"]
    assert actual == expected

def test_can_successfully_insert_a_node_after_the_last_node_of_the_linked_list():
    x = LinkedList()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.insert_after("a", "test")
    actual = x.contains()
    expected = ["e","d","c","b","a","test"]
    assert actual == expected
