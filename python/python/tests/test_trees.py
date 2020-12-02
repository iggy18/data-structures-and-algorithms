import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree


def test_con2():
    assert BinaryTree


def test_con3():
    assert BinarySearchTree


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
    expected = ["A", "B", "D", "E", "C"]
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
    actual = tree.in_order()
    expected = ["D", "B", "E", "A", "C"]
    assert actual == expected


def test_Can_successfully_return_a_collection_from_a_postorder_traversal():
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
    actual = tree.post_order()
    expected = ["D", "E", "B", "C", "A"]
    assert actual == expected


def test_can_use_add_method_to_add_to_tree():
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(6)
    actual = tree.preorder
    expected = [3, 6, 4]


def test_binary_search_tree_can_successfully_sort_values():
    pass
