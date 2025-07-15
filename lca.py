# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def find_ancestors(root, node):
            if root.val == node.val:
                return [node]

            if root.left:
                solution = find_ancestors(root.left,node)
                if solution is not None:
                    solution.append(root)
                    return solution

            if root.right:
                solution = find_ancestors(root.right,node)
                if solution is not None:
                    solution.append(root)
                    return solution

            return None

        p_ancestors = list(reversed(find_ancestors(root, p)))
        q_ancestors = list(reversed(find_ancestors(root, q)))

        scan = min(len(p_ancestors)-1, len(q_ancestors)-1)

        while scan >= 0:
            if p_ancestors[scan].val == q_ancestors[scan].val:
                return p_ancestors[scan]
            scan -= 1

        return root
