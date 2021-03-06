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

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def insert_before(self, val, new_val):
        if self.head is None:
            return "no list was created"
        if val == self.head.val:
            new_node = Node(new_val)
            new_node.next = self.head
            self.head = new_node
            return
            # have to return of else new value gets added to front of list twice
        node = self.head
        while node:
            if node.next.val == val:
                break
            node = node.next
        if node.next is None:
            return "the item you're looking for is not in the list"
        else:
            new_node = Node(new_val)
            new_node.next = node.next
            node.next = new_node

    def insert_after(self, val, new_val):
        node = self.head
        while node:
            if node.val == val:
                break
            node = node.next
        if node is None:
            return "search value is not in list"
        else:
            new_node = Node(new_val)
            new_node.next  = node.next
            node.next = new_node

    def kth_from_end(self, k):
        if not self.head:
            return "there is no list to search"
        if k < 0:
            return "you must enter a positive value"
        lead = self.head
        for i in range(k+1):
            if lead == None:
                return "k is greater than length of linked list"
            lead = lead.next
        kth = self.head
        while lead:
            lead = lead.next
            kth = kth.next
        return kth.val

def zip_lists(first, second):
    a = first.head
    zip_a = a.next
    b = second.head
    zip_b = b.next
    while a or b:
        b.next = a
        a.next = zip_b
        a = zip_a
        b = zip_b
        if a.next != None and b.next != None:
            zip_a = zip_a.next
            zip_b = zip_b.next
        else:
            b.next = a
            return second
