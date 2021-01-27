class Node:
    """
    this is the constructor.
    """
    def __init__ (self, val = None, next = None):
        self.val = val
        self.next = next


class LinkedList:
    """
    stores reference to head node, and interacts with nodes, but is not a node.
    """
    def __init__(self):
        self.head = None

    def contains(self):
        contents = []
        node = self.head
        while node:
            contents.append(node.val)
            node = node.next
        return contents

    def includes(self, val):
        node = self.head
        while node != None:
            if node.val == val:
                return True
            node = node.next
        return False

    def insert(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def __str__(self):
        node = self.head
        phrase = []
        while node != None:
            phrase.append(f'{{ ' + str(node.val) + ' }')
            node = node.next
        phrase.append("NULL")
        return " -> ".join(phrase)

new_node = LinkedList()
new_node.insert("a")
new_node.insert("b")
new_node.insert("c")
new_node.insert("d")
new_node.__str__()

