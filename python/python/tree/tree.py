class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

new_node = Node(10)


class BinaryTree:

    def __init__(self, root):
        self.root = None

    def preorder(self, start):
        """
        this method checks the the root, then left, then right
        """
        pass

    def in_order(self):
        """
        this method checks the left, then root, then right.
        """
        pass

    def post_order(self):
        """
        this method checks the left, then right, root.
        """
        pass


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add (self, data, node):
        pass

    def contains(self):
        pass
