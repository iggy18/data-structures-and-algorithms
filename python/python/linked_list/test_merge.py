from linked import Node, LinkedList, zip_lists

def test_life():
    assert zip_lists

def test_insert_multiple_node():
    x = LinkedList()
    x.insert("a")
    x.insert("c")
    x.insert("e")
    y = LinkedList()
    y.insert("b")
    y.insert("d")
    y.insert("f")
    z = zip_lists(x, y)
    actual = z.contains()
    expected =  ["f","e","d","c","b","a"]
    assert actual == expected
