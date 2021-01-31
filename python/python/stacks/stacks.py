
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class InvalidOperationError(Exception):
    pass


class Stack:


    def __init__(self):
        self.top_of_list = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_of_list
        self.top_of_list = new_node

    def pop(self):
        if not self.top_of_list:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top_of_list.value
        self.top_of_list = self.top_of_list.next
        return value

    def is_empty(self):
        if not self.top_of_list:
            return True
        return False

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top_of_list.value


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear is None:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.front.next

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("the queue is empty")
        if self.front is None:
            return Node
        else:
            to_return = self.front.value
            self.front = self.front.next
            return to_return

    def is_empty(self):
        if not self.front:
            return True
        return False


    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


