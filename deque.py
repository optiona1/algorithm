class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def size(self) -> int:
        return len(self.items)

    def remove_rear(self):
        return self.items.pop()

    def remove_front(self):
        return self.items.pop(0)

