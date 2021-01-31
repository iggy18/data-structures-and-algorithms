from tree import Node, BinaryTree, BinarySearchTree, Nope
from stacks import Queue
import pytest


def test_node():
    assert Node

def test_BinaryTree():
    assert BinaryTree

def test_binary_search_tree():
    assert BinarySearchTree

def test_queue():
    assert Queue

def test_breadth_first_raises_error_with_empty_tree():
    x = BinaryTree()
    with pytest.raises(Nope):
        x.breadth_first()

def test_breadth_first_properly_walks_through_and_collects_values():
    x = BinaryTree()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    x.root = a
    x.root.left = b
    x.root.right = c
    x.root.left.left = d
    x.root.left.right = e
    x.root.right.left = f
    actual = x.breadth_first()
    expected = [1,2,3,4,5,6]
    assert actual == expected

def test_breadth_first_properly_walks_through_and_collects_values_in_asym_tree():
    x = BinaryTree()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(8)
    i= Node(9)
    x.root = a
    x.root.left = b
    x.root.right = c
    x.root.left.left = d
    x.root.left.right = e
    x.root.left.left.left = f
    x.root.left.left.right= g
    x.root.right.right = h
    x.root.right.right.right = i
    actual = x.breadth_first()
    expected = [1,2,3,4,5,8,6,7,9]
    assert actual == expected


