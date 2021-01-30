class InvalidOperationError(Exception):
    pass

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:

    def __init__(self, front, back):
        self.front = front
        self.back = back

    def enqueue(self, val):
        node = Node(val)
        if not self.front:
            self.front = node
            self.back = node
            return
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError()
        else:
            pop_node = self.front
            self.front = pop_node.next
            return pop_node.val

    def is_empty(self):
        if not self.front:
            return True
        else:
            return False

    def peek(self):
        if not self.front:
            raise InvalidOperationError()
        else:
            return self.front.val



























