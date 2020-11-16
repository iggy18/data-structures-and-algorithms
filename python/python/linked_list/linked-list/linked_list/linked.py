class Node:
    """
    this is the constructor.
    """
    def __init__ (self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    """
    this is the head node.
    """
    def __init__(self):
        self.head = None

    def includes(self, data):
        node = self.head
        while node != None:
            if node.data == data:
                return True
            node = node.next
        return False

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def __str__(self):
        node = self.head
        phrase = []
        while node != None:
            phrase.append(f'[ ' +node.data+ ' ]')
            node = node.next
        phrase.append("NUll")
        return " -> ".join(phrase)
