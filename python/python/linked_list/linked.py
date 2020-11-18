class Node:
    """
    this is the constructor.
    """
    def __init__ (self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    """
    stores reference to head node, and interacts with nodes, but is not a node.
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

    # def insert_after(self, current_node, data):
    #     pass
    #     check = self.head
    #     while check is not None:
    #         if check.data == current_node.data
    #             break
    #         check = check.next
    #     if check is None
    #         print("not in list")
    #     else:
    #         new_node = Node(data)
    #         new_node.next = check.next
    #         check.next = new_node

    def __str__(self):
        node = self.head
        phrase = []
        while node != None:
            phrase.append(f'[ ' +node.data+ ' ]')
            node = node.next
        phrase.append("NUll")
        return " -> ".join(phrase)

new_node = LinkedList()
new_node.insert("a")
new_node.insert("b")
new_node.insert("c")
new_node.insert("d")
new_node.__str__()

