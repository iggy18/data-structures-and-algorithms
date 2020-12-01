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
        # this calls the walk function and passes the root as the peramimter
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
        if value < root.value:
            if not root.left:
                root.left = node
            else:
                pass
        else:
            if not root.right:
                root.right = node
            else:
                pass
    walk(self.root)

    def contains(self, value):
        def walk(node):
            if not node:
                return False
            if node.value == value:
                return True
            else:
                """
                if the value in less than nodes value look left
                """
                if value < node.value:
                    # walk function wants a node, so you will pass it a node.
                    return walk(node.left)
                else:
                    return walk(node.right)
        found = walk(self.root)
        return found


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
