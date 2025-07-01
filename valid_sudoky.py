class Solution:
    def isValidSudoku(self, board):
        def is_valid(i, numbers):
            if i != ".":
                if i in numbers:
                    return False
                else:
                    numbers.add(i)

            return True

        # Check rows
        for row in board:
            numbers = set()
            for i in row:
                print(i, end=", ")
                if not is_valid(i, numbers):
                    return False

            print("")

        print("")

        # Check cols
        for y in range(len(board)):
            numbers = set()
            for x in range(len(board)):
                print(board[x][y], end=", ")
                if not is_valid(board[x][y], numbers):
                    return False

            print("")

        print("")

        # Check centers
        n = len(board) // 3
        for center_y in range(n):
            for center_x in range(n):
                numbers = set()
                x, y = center_y*3, center_x*3
                for delta_y in [0,1,2]:
                    for delta_x in [0,1,2]:
                        if not is_valid(board[y+delta_y][x+delta_x], numbers):
                            return False

        return True

solver = Solution()
print(solver.isValidSudoku(
    [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]))
