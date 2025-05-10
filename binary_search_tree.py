class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    def __init__(self, root: TreeNode):
        self._root = root

    def searchRecur(self, num: int) -> TreeNode | None:
        root = self._root
        if num == root.val:
            return root

        if root.val < num:
            return self.search(root.right)
        else:
            return self.search(root.left)

    def search(self, num: int) -> TreeNode | None:
        cur = self._root
        while cur is not None:
            if cur.val < num:
                cur = cur.right
            elif cur.val > num:
                cur = cur.left
            else:
                break
        return cur

    def insert(self, num: int):
        if self._root is None:
            self._root = TreeNode(num)
            return

        cur, pre = self._root, None
        while cur is not None:
            if cur.val == num:
                return
            pre = cur

            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left

        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node
            

    def remove(self, num: int):
        if self._root is None:
            return

        cur, pre = self._root, None
        while cur is not None:
            if cur.val == num:
                break
            pre = cur
            if cur.val < num:
                cur = cur.right
            else:
                cur = cur.left

        if cur is None:
            return

        if cur.left is None or cur.right is None:
            child = cur.left or cur.right
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                self._root = child

        else:
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left

            self.remove(tmp.val)
            cur.val = tmp.val
