from tree import BinaryTree, Node
from tree_intersection import tree_intersection
import pytest
from collections import Counter

def test_node():
    assert Node

def test_binary_tree():
    assert BinaryTree

def test_tree_intersection():
    assert tree_intersection

def test_intersections_with_one():
    x = BinaryTree()
    y = BinaryTree()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("A")
    e = Node("E")
    f = Node("F")
    x.root = a
    x.root.left = b
    x.root.right = c
    y.root = d
    y.root.left = e
    y.root.right = f
    actual = tree_intersection(x,y)
    expected = ["A"]
    assert actual == expected

def test_intersections_with_multiple():
    x = BinaryTree()
    y = BinaryTree()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("A")
    e = Node("B")
    f = Node("F")
    x.root = a
    x.root.left = b
    x.root.right = c
    y.root = d
    y.root.left = e
    y.root.right = f
    actual = Counter(tree_intersection(x,y))
    expected = Counter(["B","A"])
    assert actual == expected

def test_intersections_with_all_dupes():
    x = BinaryTree()
    y = BinaryTree()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("A")
    e = Node("B")
    f = Node("C")
    x.root = a
    x.root.left = b
    x.root.right = c
    y.root = d
    y.root.left = e
    y.root.right = f
    actual = Counter(tree_intersection(x,y))
    expected = Counter(["C","B","A"])
    assert actual == expected

def test_intersections_with_NO_dupes():
    x = BinaryTree()
    y = BinaryTree()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    x.root = a
    x.root.left = b
    x.root.right = c
    y.root = d
    y.root.left = e
    y.root.right = f
    actual = tree_intersection(x,y)
    expected = []
    assert actual == expected

def test_intersections_with_empty_trees():
    x = BinaryTree()
    y = BinaryTree()
    actual = tree_intersection(x,y)
    expected = []
    assert actual == expected
