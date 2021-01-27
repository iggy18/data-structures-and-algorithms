
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
        value = self.top_of_stack.value
        self.top_of_stack = self.top_of_stack.next
        return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        return self.top_of_stack.value


class Pseudo_Queue():

    __init__(self):
        self.first_stack = stack()
        self.second_stack = stack()

    enqueue(self, value):
        if first_stack == None:
            self.first_stack.push(value)
            return
        while self.first_stack.top_of_stack:
            top = self.first_stack.pop()
            self.second_stack.push(top)
        self.second_stack.push(value)

    dequeue(self, value):
        return self.first_stack.pop()
