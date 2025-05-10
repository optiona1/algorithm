class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def enqueue(self, value):
        self.item.append(value)

    def size(self) -> int:
        return len(self.item)

    def dequeue(self):
        return self.item.pop()

