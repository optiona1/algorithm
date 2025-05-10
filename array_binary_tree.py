class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        self._tree = list(arr)

    def size(self) -> int:
        return len(self._tree)

    def val(self, i: int) -> int | None:
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                res.append(self.val(i))
        return res

    def dfs(self, i: int, order: str):
        if self.val(i) is None:
            return

        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)

        if order == "in":
            self.res.append(self.val(i))

        self.dfs(self.right(i), order)

        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="pre")
        return self.res

    def in_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="in")
        return self.res

    def post_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="post")
        return self.res

if __name__ == '__main__':
    tree = ArrayBinaryTree()
    
