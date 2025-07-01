class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] != 0:
                continue

            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] != 0:
                continue

            for i in range(len(matrix)):
                matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

            for i in range(len(matrix)):
                matrix[i][0] = 0


solver = Solution()
matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(solver.setZeroes(matrix))
print(matrix)
