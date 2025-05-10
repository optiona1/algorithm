class ArrayQueue:
    def __init__(self, size: int):
        self._nums: list[int] = [0] * size
        self._front: int = 0
        self._size: int = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def enqueue(self, val: int):
        if self._size == len(self._nums):
            raise IndexError("队列已满")
        self._nums[(self._size + self._front) % len(self._nums)] = val
        self._size += 1

    def dequeue(self) -> int:
        num = self.peek()
        self._front = (self._front + 1) % len(self._nums)
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("队列为空")
        return self._nums[self._front]

    def to_list(self) -> list[int]:
        arr = []
        for i in range(self._front, self._front + self._size):
            arr.append(self._nums[i % len(self._nums)])

        return arr
            
    


if __name__ == '__main__':
    queue = ArrayQueue(10)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.to_list())
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    print(queue.to_list())
    assert queue.dequeue() == 3
    print(queue.to_list())
    assert queue.is_empty() is True
