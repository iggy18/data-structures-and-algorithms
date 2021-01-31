from tree import Node, BinaryTree

def test_node():
    assert Node

def test_binary_tree():
    assert BinaryTree

def test_find_maximum_value_returns_max_value():
    a = Node(4)
    b = Node(2)
    c = Node(8)
    d = Node(42)
    e = Node(18)
    f = Node(12)
    g = Node(25)
    h = Node(7)
    x = BinaryTree()
    x.root = a
    x.root.left = b
    x.root.right = c
    x.root.left.left = d
    x.root.left.right = e
    x.root.right.left = f
    x.root.right.right = h
    actual = x.max_value()
    expected = 42
    assert actual == expected

def test_find_maximum_value_works_with_negative():
    a = Node(4)
    b = Node(2)
    c = Node(8)
    d = Node(-42)
    e = Node(18)
    f = Node(12)
    g = Node(25)
    h = Node(7)
    x = BinaryTree()
    x.root = a
    x.root.left = b
    x.root.right = c
    x.root.left.left = d
    x.root.left.right = e
    x.root.right.left = f
    x.root.right.right = g
    x.root.right.right.right = h
    actual = x.max_value()
    expected = 25
    assert actual == expected

def test_find_maximum_value_works_with_ALL_negative():
    a = Node(-4)
    b = Node(-2)
    c = Node(-8)
    d = Node(-42)
    e = Node(-18)
    f = Node(-12)
    g = Node(-25)
    h = Node(-7)
    x = BinaryTree()
    x.root = a
    x.root.left = b
    x.root.right = c
    x.root.left.left = d
    x.root.left.right = e
    x.root.right.left = f
    x.root.right.right = g
    x.root.right.right.right = h
    actual = x.max_value()
    expected = -2
    assert actual == expected

def test_max_value_works_with_unbalanced_tree():
    a = Node(4)
    b = Node(2)
    c = Node(8)
    d = Node(42)
    e = Node(18)
    f = Node(12)
    g = Node(68)
    h = Node(70)
    x = BinaryTree()
    x.root = a
    x.root.left = b
    x.root.left.left = c
    x.root.left.left.left = d
    x.root.left.left.right = e
    x.root.left.left.left.left = f
    x.root.left.left.left.right = g
    x.root.left.left.left.left.left = h
    actual = x.max_value()
    expected = 70
    assert actual == expected

def test_max_returns_zero_for_empty_tree():
    x = BinaryTree()
    actual = x.max_value()
    expected = 0
    assert actual == expected
