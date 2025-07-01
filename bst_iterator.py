# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.root = root

    def next(self):
        next, self.root = self.get_next(self.root, pop=True)
        return next

    def hasNext(self):
        next, _ = self.get_next(self.root)
        return next is not None

    def get_next(self, current, pop=False):
        if current is None:
            return None, None

        if current.left is None and current.right is None:
            return current, None

        if current.left is not None:
            next, left = self.get_next(current.left)
            if pop:
                current.left = left

            return next,current
        else:
            next, right = self.get_next(current.right)
            if pop:
                current.right = right

            return next, current



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
