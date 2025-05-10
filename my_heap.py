class Heap:
    def __init__(self, nums: list[int]):
        self.max_heap = nums
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    def size(self) -> int:
        return len(self.max_heap)

    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def peek(self) -> int:
        return self.max_heap[0]

    def is_empty(self) -> bool:
        return self.size() == 0

    def swap(self, a: int, b: int):
        self.max_heap[a], self.max_heap[b] = self.max_heap[b], self.max_heap[a]

    def push(self, val: int):
        self.max_heap.append(val)
        self.sift_up(self.size() - 1)

    def sift_up(self, i: int):
        while True:
            p = self.parent(i)
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break

            self.swap(i, p)
            i = p

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("堆为空")

        self.swap(0, self.size() - 1)
        val = self.max_heap.pop()
        self.sift_down(0)
        return val

    def sift_down(self, i: int):
        while True:
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r

            if ma == i:
                break

            self.swap(i, ma)
            i = ma
