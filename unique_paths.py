class Solution:
    def uniquePaths(self, m, n):
        paths = [[0] * n for _ in range(m)]

        for y in reversed(range(m)):
            for x in reversed(range(n)):
                unique_from_position = 1
                if y == m-1 and x == n-1:
                    unique_from_position = 1
                elif y == m-1:
                    unique_from_position = paths[y][x+1]
                elif x == n-1:
                    unique_from_position = paths[y+1][x]
                else:
                    unique_from_position = paths[y+1][x]+ paths[y][x+1]

                paths[y][x] = unique_from_position

        return paths[0][0]

solver = Solution()
print(solver.uniquePaths(3,2))
