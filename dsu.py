# 并查集
#

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1


class QuickFindUF:
    # 快速查找的并查集
    # 初始化复杂度：O(n)
    # 联通判断复杂度：O(1)
    # 合并复杂度：O(n)
    def __init__(self, n):
        # self.id = [0] * n
        # for i in range(n):
        #     self.id[i] = i
        self.id = list(range(n))

    def connected(self, p: int, q: int) -> bool:
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int) -> None:
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid


class QuickUnionUF:
    def __init__(self, n):
        self.id = list(range(n))

    def _root(self, i: int) -> int:
        while i != self.id[i]:
            i = self.id[i]

        return i

    def connected(self, p: int, q: int) -> bool:
        return self._root(p) == self._root(q)

    def union(self, p: int, q: int) -> None:
        i = self._root(p)
        j = self._root(q)
        self.id[i] = j


if __name__ == '__main__':
    dsu = DSU(10)
    dsu.union(0, 1)
    dsu.union(1, 2)
    print(dsu.find(2))

