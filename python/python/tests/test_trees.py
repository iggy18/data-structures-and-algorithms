import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree

def test_con():
    assert Node

def test_con2():
    assert BinaryTree

def test_con3():
    assert BinarySearchTree




def test_Can_successfully_instantiate_an_empty_tree():
    tree = BinaryTree(1)
    assert tree

@pytest.mark.skip
def test_Can_successfully_instantiate_a_tree_with_a_single_root_node():
    pass

@pytest.mark.skip
def test_Can_successfully_add_a_left_child_and_right_child_to_a_single_root_node():
    pass

@pytest.mark.skip
def test_Can_successfully_return_a_collection_from_a_preorder_traversal():
    pass

@pytest.mark.skip
def test_Can_successfully_return_a_collection_from_an_inorder_traversal():
    pass

@pytest.mark.skip
def test_Can_successfully_return_a_collection_from_a_postorder_traversal():
    pass
