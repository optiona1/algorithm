class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

        
class HashMapOpenAddressing:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets: list[Pair | None] = [None] * self.capacity
        self.TOMBSTONE = Pair(-1, "-1")

    def hash_func(self, key: int) -> int:
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def find_bucket(self, key: int) -> int:
        index = self.hash_func(key)
        first_tombstone = -1
        while self.buckets[index] is not None:
            if self.buckets[index].key == key:
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone
                return index
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index

            index = (index + 1) % self.capacity

        return index if first_tombstone == -1 else first_tombstone

    def get(self, key: int) -> str:
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val

        return None

    def put(self, key: int, val: str):
        if self.load_factor() > self.load_thres:
            self.extend()

        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return

        self.buckets[index] = Pair(key, val)
        self.size += 1

    def remove(self, key: int):
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1

    def extend(self):
        buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [None for _ in range(self.capacity)]
        self.size = 0

        for pair in buckets:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.val)

    def print(self):
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(pair.key, "->", pair.val)


if __name__ == '__main__':
    m = HashMapOpenAddressing()
    m.put(1, 'a')
    m.put(2, 'b')
    m.put(3, 'c')
    m.put(4, 'd')
    m.put(5, 'e')
    m.put(2, 'bb')
    assert m.get(2) == 'bb'
    print(m.size)
    assert m.size == 5
    m.remove(4)

    assert m.get(4) is None
    assert m.size == 4
    m.print()
 
