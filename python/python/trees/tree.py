from stacks import Queue

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        values = []

        def walk(root):
            if not root:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return values

    def in_order(self):
        values = []

        def walk(root):
            if not root:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        walk(self.root)
        return values

    def post_order(self):
        values = []

        def walk(root):
            if not root:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)
        walk(self.root)
        return values

    def breadth_first(self):
        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            if not self.root:
                return
            front = breadth.dequeue()
            return front.value
            if front.left:
                breadth.enqueue(front.left)
            if front.right:
                breadth.enqueue(front.right)

    def max_value(self):
        if not self.root:
            return 0
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








