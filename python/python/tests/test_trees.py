import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree

def test_con():
    assert Node

def test_con2():
    assert BinaryTree

def test_con3():
    assert BinarySearchTree


a = Node("A")  # this assigns value to the node
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

f = Node("12")
g = Node("20")
h = Node("6")
i = Node("7")
j = Node("42")

def test_Can_successfully_instantiate_an_empty_tree():
    tree = BinaryTree()
    assert tree

def test_Can_successfully_instantiate_a_tree_with_a_single_root_node():
    tree = BinaryTree()
    a = Node("A")
    tree.root = a
    actual = tree.root.value
    expected = "A"
    assert actual == expected


def test_Can_successfully_add_a_left_child_and_right_child_to_a_single_root_node():
    pass
    a = Node("A")  # this assigns value to the node
    b = Node("B")
    c = Node("C")
    tree = BinaryTree()  # this makes the binary tree
    tree.root = a
    a.left = b
    a.right = c
    actual = a.left.value, a.right.value
    expected = "B", "C"
    assert actual == expected

@pytest.mark.skip
def test_Can_successfully_return_a_collection_from_a_preorder_traversal():
    pass
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    tree = BinaryTree()
    tree.root = a
    a.left = b
    a.right = c
    a.left.left = d
    a.left.right = e
    actual = tree.preorder()
    expected = "A", "B", "D", "E", "C"
    assert actual == expected


def test_Can_successfully_return_a_collection_from_an_inorder_traversal():
    a = Node("A")  # this assigns value to the node
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    tree = BinaryTree()  # this makes the binary tree
    tree.root = a
    a.left = b
    a.right = c
    a.left.left = d
    a.left.right = e
    actual = tree.inorder()
    expected = "D", "B", "E", "A", "C"
    assert actual == expected
@pytest.mark.skip
def test_Can_successfully_return_a_collection_from_a_postorder_traversal():
    pass
    """
    actual =
    expected =
    assert actual == expected
    """
"""
a = Node("A")  # this assigns value to the node
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

tree = BinaryTree()  # this makes the binary tree
tree.root = a
a.left = b
a.right = c
a.left.left = d
a.left.right = e
tree.preorder()
tree.in_order()
tree.post_order()
"""
