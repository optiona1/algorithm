class ArrayDeque:
    def __init__(self, capacity: int):
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._nums)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.size() == 0

    def index(self, i: int) -> int:
        return (i + self.capacity()) % self.capacity()

    def push_first(self, val: int):
        if self._size == self.capacity():
            raise IndexError("双向队列已满")
        index = self.index(self._front - 1)
        self._nums[index] = val
        self._front = index
        self._size += 1

    def push_last(self, val: int):
        if self._size == self.capacity():
            raise IndexError("双向队列已满")
        index = self.index(self._front + self._size)
        self._nums[index] = val
        self._size += 1
        
    def pop_first(self) -> int:
        num = self._nums[self._front]
        self._front = self.index(self._front + 1)
        self._size -= 1
        return num

    def pop_last(self) -> int:
        num = self.peek_last()
        self._size -= 1
        return num

    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError("双向队列为空")

        return self._nums[self._front]

    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError("双向队列为空")
        last = self.index(self._front + self._size - 1)
        return self._nums[last]

    def to_list(self) -> list[int]:
        arr = []
        for i in range(self._size):
            arr.append(self._nums[self.index(self._front + i)])
        return arr
        
        



if __name__ == '__main__':
    deque = ArrayDeque(10)
    deque.push_last(3)
    deque.push_first(4)
    deque.push_first(5)
    deque.push_first(6)
    print(deque.to_list())
    assert deque.pop_first() == 6
    assert deque.pop_last() == 3
    print(deque.to_list())
