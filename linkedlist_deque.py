class LinkedNode:
    def __init__(self, val: int):
        self.val: int = val
        self.prev: LinkedNode | None = None
        self.next: LinkedNode | None = None

    def __repr__(self):
        return f'{self.val}'

class LinkedListDeque:
    def __init__(self):
        self._front: LinkedNode | None = None
        self._rear: LinkedNode | None= None
        self._size: int = 0

    def is_emtpy(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return self._size

    def push_first(self, val: int):
        node = LinkedNode(val)
        if self.is_emtpy():
            self._front = node
            self._rear = node
        else:
            node.next = self._front
            self._front.prev = node
            self._front = node
        self._size += 1

    def push_last(self, val: int):
        node = LinkedNode(val)
        if self.is_emtpy():
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def peek_first(self) -> int:
        if self.is_emtpy():
            raise IndexError("队列为空")

        return self._front.val

    def peek_last(self) -> int:
        if self.is_emtpy():
            raise IndexError("队列为空")

        return self._rear.val

    def pop_first(self) -> int:
        num = self.peek_first()
        self._front = self._front.next
        self._front.prev = None
        self._size -= 1
        return num

    def pop_last(self) -> int:
        num = self.peek_last()
        temp = self._rear.prev
        self._rear.prev = None
        self._rear = temp
        self._size -= 1
        return num

    def to_list(self) -> list[int]:
        arr = []
        node = self._front
        while node:
            arr.append(node.val)
            node = node.next

        return arr

        
if __name__ == '__main__':
    deque = LinkedListDeque()
    deque.push_last(3)
    deque.push_first(4)
    deque.push_first(5)
    deque.push_first(6)
    print(deque.to_list())
    assert deque.pop_first() == 6
    assert deque.pop_last() == 3
    print(deque.to_list())
