class Solution:
    def minPathSum(self, grid):
        # Could I do it in place?
        m, n = len(grid), len(grid[0])

        interim = [[0] * m for _ in range(n)]

        for y in reversed(range(m)):
            for x in reversed(range(n)):
                min_sum = 0
                if y == m-1 and x == n-1:
                    min_sum = 0
                elif x == n-1:
                    min_sum = interim[y+1][x]
                elif y == m-1:
                    min_sum = interim[y][x+1]
                else:
                    min_sum = min(interim[y+1][x], interim[y][x+1])

                interim[y][x] = grid[y][x] + min_sum

        return interim[0][0]

grid = [[1,3,1],[1,5,1],[4,2,1]]
solver = Solution()
print(solver.minPathSum(grid))
