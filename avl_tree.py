class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.height: int = 0
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class AVLTree:
    def __init__(self):
        self._root = None

    def height(self, node: TreeNode | None) -> int:
        if node is not None:
            return node.height
        return -1

    def update_height(self, node: TreeNode | None):
        node.height = max([self.height(node.left), self.height(node.right)]) + 1

    def balance_factor(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
        child = node.left
        grand_child = child.right
        child.right = node
        node.left = grand_child
        self.update_height(node)
        self.update_height(child)
        return child

    def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
        child = node.right
        grand_child = child.left
        child.left = node
        node.right = grand_child
        self.update_height(node)
        self.update_height(child)
        return child

    def rotate(self, node: TreeNode| None) -> TreeNode | None:
        banlance_factor = self.balance_factor(node)
        if banlance_factor > 1:
            if self.balance_factor(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        elif banlance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        return node

    def insert(self, val):
        self._root = self.insert_helper(self._root, val)

    def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self.insert_helper(node.left, val)
        elif val > node.val:
            node.right = self.insert_helper(node.right, val)
        else:
            return node

        self.update_height(node)
        return self.rotate(node)

    def remove(self, val: int):
        self._root = self.remove_helper(self._root, val)

    def remove_helper(self, node: TreeNode | None, val) -> TreeNode | None:
        if node is None:
            return None

        if val < node.val:
            node.left = self.remove_helper(node.left, val)
        elif val > node.val:
            node.right = self.remove_helper(node.right, val)
        else:
            if node.left is None or node.right is None:
                child = node.left or node.right
                if child is None:
                    return None

                else:
                    node = child
            else:
                temp = node.right
                while temp.left is not None:
                    temp = temp.left

                node.right = self.remove_helper(node.right, temp.val)
                node.val = temp.val
        
