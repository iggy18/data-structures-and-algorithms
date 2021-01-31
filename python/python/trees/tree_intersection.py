from stacks import Queue
from tree import BinaryTree
from random import randint


def tree_intersection(treeOne, treeTwo):
    identical = []
    tree_one = TreeOne.pre_order()
    tree_two = TreeTwo.pre_order()
    for potential_identical in tree_one:
        if potential_identical in tree_two:
            identical.append(potential_identical)
    return identical
