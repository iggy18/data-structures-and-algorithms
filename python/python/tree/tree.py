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
        return values

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
        return values

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
        return values

    def max_value(self):

        max_value = self.root.value

        def walk(root):
            nonlocal max_value

            if root.value > max_value:
                max_value = root.value
            if root.left:
                walk(root.left)
            if root.right:
                walk(root.right)
        walk(self.root)
        return max_value


class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root = None

    def add(self, value):
        """
        """
        node = Node(value)

        def walk(root):
            if not root:
                self.root = node
                return
            if root.value > value:
                if not root.left:
                    root.left = node
                else:
                    walk(root.left)
            else:
                if not root.right:
                    root.right = node
                else:
                    walk(root.right)
        walk(self.root)

    def contains(self, value):
        """
        search tree for a given value return true if found else false.
        """
        def walk(root):
            if not root:
                return False
            if root.value == value:
                return True
            else:
                if root.value > value:
                    return walk(root.left)
                else:
                    return walk(root.right)
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
print("preorder", tree.preorder())
print("in order", tree.in_order())
print("post", tree.post_order())

tree = BinarySearchTree()
tree.add(4)
tree.add(9)
tree.add(2)
tree.add(42)
tree.add(3)
tree.add(15)
tree.add(1)
tree.add(21)
actual = tree.preorder()
print("binary preorder", tree.preorder())
