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

def test_dif_length_lists():
    x = LinkedList()
    x.insert("4")
    x.insert("3")
    x.insert("2")
    x.insert("1")
    x.insert("a")
    x.insert("c")
    x.insert("e")
    y = LinkedList()
    y.insert("b")
    y.insert("d")
    y.insert("f")
    z = zip_lists(x, y)
    actual = z.contains()
    expected =  ["f","e","d","c","b","a","1","2","3","4"]
    assert actual == expected
