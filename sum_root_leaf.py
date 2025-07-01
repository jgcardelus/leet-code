## There's a much simpler way to solve this

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        def merge_numbers(node, numbers, children):
            for child_number in children:
                child_number.append(node.val)
                numbers.append(child_number)

        def dfs(node):
            if node is None:
                return []

            if node.left is None and node.right is None:
                return [node.val]

            numbers = []

            if node.left:
                child_numbers = dfs(node.right)
                merge_numbers(node, numbers, child_numbers)

            if node.right:
                child_numbers = dfs(node.right)
                merge_numbers(node, numbers, child_numbers)

            return numbers

        combinations = dfs(root)

        def to_number(combination):
            number = 0
            for i, num in enumerate(combination):
                number += num * (10**i)

            return number

        acc = 0
        for combination in combinations:
            acc += to_number(combination)

        return acc

solver = Solution()
print(solver.sumNumbers(None))
