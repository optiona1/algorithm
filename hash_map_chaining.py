class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

        
class HashMapChaining:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_func(self, key: int) -> int:
        return key % self.capacity

    def load_factor(self) -> float:
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val

        return None

    def put(self, key: int, val: str):
        if self.load_factor() > self.load_thres:
            self.extend()

        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return

        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1
                
    def remove(self, key: int):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        for bucket in self.buckets:
            res = []
            if bucket == []:
                continue
            for pair in bucket:
                res.append(str(pair.key) + " -> " + pair.val)
            print(res)


if __name__ == '__main__':
    m = HashMapChaining()
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
 
