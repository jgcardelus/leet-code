class Solution:
    def generateParenthesis(self, n):
        result = []

        def dfs(left, right, current):
            if len(current) == n * 2:
                result.append(current)

            if left < n:
                dfs(left + 1, right, current + "(")

            if right < left:
                dfs(left, right + 1, current + ")")

        dfs(0,0,"")
        return result
