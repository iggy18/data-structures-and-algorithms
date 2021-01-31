class InvalidOperationError(Exception):
    pass

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        node = Node(val)
        if self.rear is None:
            self.front = node
            self.rear = self.front
        else:
            self.rear.next = node
            self.rear = self.front.next

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("there are no critters here today")
        else:
            pop_node = self.front.val
            self.front = self.front.next
            return pop_node

    def is_empty(self):
        if not self.front:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("there are no critters here today")
        else:
            return self.front.val


class AnimalShelter:

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, val):
        if val == "cat":
            kitty = self.cats.enqueue(val)

        elif val == "dog":
            doggy = self.dogs.enqueue(val)
        else:
            raise InvalidOperationError("what is that?")

    def dequeue(self, preference=None):
        if preference == "cat":
            kitty = self.cats.dequeue()
            return kitty

        if preference == "dog":
            doggy = self.dogs.dequeue()
            return doggy
        else:
            return None























