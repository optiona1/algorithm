class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

    def __repr__(self):
        return f'{self.key}: {self.val}'


class ArrayHashMap:
    def __init__(self):
        self._pair: list[Paire | None] = [None] * 100

    def hash(self, key: int) -> int:
        return key % 100
        

    def put(self, key: int, val: str):
        self._pair[self.hash(key)] = Pair(key, val)

    def get(self, key: int) -> str | None:
        pair = self._pair[self.hash(key)]
        if pair:
            return pair.val
        return None

    def delete(self, key):
        pair = self._pair[self.hash(key)]
        if pair:
            self._pair[self.hash(key)] = None

    def items(self) -> list[Pair]:
        result: list[Pair] = []
        for pair in self._pair:
            if pair is not None:
                result.append(pair)
        return result

    def keys(self) -> list[int]:
        result: list[int] = []
        for pair in self._pair:
            if pair is not None:
                result.append(pair.key)
        return result
            
    def values(self) -> list[str]:
        result: list[str] = []
        for pair in self._pair:
            if pair is not None:
                result.append(pair.val)
        return result
            
    def print(self):
        for pair in self._pair:
            if pair is not None:
                print(pair.key, "->", pair.val)


if __name__ == '__main__':
    m = ArrayHashMap()
    m.put(1, 'a')
    m.put(2, 'b')
    m.print()
    print(m.items())
    assert m.keys() == [1, 2]
    assert m.values() == ['a', 'b']
    assert m.get(2) == 'b'
    m.delete(1)
    m.print()
