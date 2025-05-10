class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

        
def pre_order(root: TreeNode | None, res=[]):
    if root is None:
        return res
    res.append(root.val)
    res += pre_order(root.left, res)
    res += pre_order(root.right, res)
    

def in_order(root: TreeNode | None, res=[]):
    if root is None:
        return res

    res += pre_order(root.left, res)
    res.append(root.val)
    res += pre_order(root.right, res)


def post_order(root: TreeNode | None, res=[]):
    if root is None:
        return res

    res += post_order(root.left)
    res += post_order(root.left)
    res.append(root.val)
