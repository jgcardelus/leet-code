# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node is None:
                return [node, node]

            left_head, left_tail = None, None
            if node.left:
                left_head, left_tail = dfs(node.left)

            right_head, right_tail = None, None
            if node.right:
                right_head, right_tail = dfs(node.right)

            if left_head and left_tail:
                left_tail.right = right_head
            else:
                left_head = right_head

            node.right = left_head
            node.left = None

            return [node, right_tail]

        return dfs(root)
