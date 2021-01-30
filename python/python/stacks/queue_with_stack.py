class InvalidOperationError(Exception):
    pass

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top_of_stack = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_of_stack
        self.top_of_stack = new_node

    def pop(self):
        if self.top_of_stack:
            value = self.top_of_stack.value
            self.top_of_stack = self.top_of_stack.next
            return value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        else:
            return self.top_of_stack.value

    def is_empty(self):
        if not self.top_of_stack:
            return True
        return False


class Pseudo_Queue():

    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, value):
        if self.first_stack == None:
            Stack.push(value)
            return

        while self.first_stack.top_of_stack:
            top = self.first_stack.pop()
            self.second_stack.push(top)
        self.second_stack.push(value)

        while self.second_stack.top_of_stack:
            top = self.second_stack.pop()
            self.first_stack.push(top)

    def dequeue(self):
        if not self.first_stack.top_of_stack:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.first_stack.pop()

