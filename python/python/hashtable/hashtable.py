from linked import Node, LinkedList

class HashTable:
    def __init__(self, size = 1024):
        self.size = size
        self.buckets = [None]

    def set(self, key, value):
        hash_number = self.hash(key)

        if not self.buckets[hash_number]:
            self.buckets[hash_number] = LinkedList()
        self.buckets[hash_number].add((key, value))

    def get(self, key):
        hash_number = self.hash(key)
        bucket = self.buckets[hash_number]
        current = bucket.head
        while current:
            pair = current.data
            stored_key = pair[0]
            stored_value = pair[1]
            if stored_key == key:
                return stored_value
            current = current.next

    def contains(self, key):
        hash_number = self.hash(key)
        bucket = self._buckets[hash_number]
        if not bucket:
            return False
        current = bucket.head
        while current and current.value[0] != key:
            current = current.next
        if not current:
            return False
        return True

    def hash(self, key):
        num = 0
        for char in key:
            num += ord(char)
        prime = num * 19
        idx = prime %self.size
        return idx


