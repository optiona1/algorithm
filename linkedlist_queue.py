class LinkedNode:
    def __init__(self, val):
        self.val: int = val
        self.next: LinkedNode | None = None

class LinkedListQueue:
    def __init__(self):
        self._front: LinkedNode | None = None
        self._rear: LinkedNode | None = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def enqueue(self, val: int):
        node = LinkedNode(val)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def dequeue(self) -> int:

        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")            
        return self._front.val

    def to_list(self) -> list[int]:
        node = self._front
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr



if __name__ == '__main__':
    queue = LinkedListQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.to_list())
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty() is True


