class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        """
        this method checks the root, then left, then right
        """
        values = []

        def walk(root):  # recursive
            if not root:
                return
            # you can rearrange the steps below to get the other traversals
            values.append(root.value)
            walk(root.left)  # recursive
            walk(root.right)  # recursive
        walk(self.root)
        print(values)

    def in_order(self):
        """
        this method checks the left, then root, then right.
        """
        values = []

        def walk(root):  # recursive
            if not root:
                return
            # you can rearrange the steps below to get the other traversals
            walk(root.left)  # recursive
            values.append(root.value)
            walk(root.right)  # recursive
        walk(self.root)
        print(values)

    def post_order(self):
        """
        this method checks the left, then right, root.
        """
        values = []

        def walk(root):  # recursive
            if not root:
                return
            # you can rearrange the steps below to get the other traversals
            walk(root.left)  # recursive
            walk(root.right)  # recursive
            values.append(root.value)
        walk(self.root)
        print(values)


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def add(self, value):
        pass

    def contains(self):
        pass


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
