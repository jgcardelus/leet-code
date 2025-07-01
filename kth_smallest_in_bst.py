from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        count = 0
        solution = -1

        def dfs(node):
            nonlocal count
            nonlocal solution

            if node.left is None and node.right is None:
                count += 1
                if count == k:
                    solution = node.val
                    return True
                return False

            if node.left and dfs(node.left):
                return True

            count += 1
            if count == k:
                solution = node.val
                return True

            if node.right and dfs(node.right):
                return True

            return False

        dfs(root)
        return solution
