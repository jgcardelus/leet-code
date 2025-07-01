class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        root = preorder[0]
        root_index = 0

        for i, node in enumerate(inorder):
            if node == root:
                root_index = i
                break

        if len(preorder) == 2:
            if root_index == 0:
                return TreeNode(root, None, TreeNode(preorder[1], None, None))
            else:
                return TreeNode(root, TreeNode(preorder[1], None, None), None)

        if root_index == 0:
            # Where at a leaf
            return TreeNode(root, None, None)
        else:
            left = self.buildTree(preorder[1:root_index+1], inorder[0:root_index])
            right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
            return TreeNode(root, left, right)
