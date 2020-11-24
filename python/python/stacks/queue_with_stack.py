
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top_of_list = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top_of_list
        self.top_of_list = new_node

    def pop(self):
        value = self.top_of_list.value
        self.top_of_list = self.top_of_list.next
        return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top_of_list.value


class pseudo_Queue():

    __init__(self):
        self.first_stack = stack()
        self.second_stack = stack()

    enqueue(self, value):
        

    dequeue(self, value):
        pass
