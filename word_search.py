class Solution:
    def exist(self, board, word):
        def findNeighbors(i,j):
            return [
                (i-1,j),
                (i+1,j),
                (i,j-1),
                (i,j+1),
            ]

        def dfs(board, i, j, current):
            if not (0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] != "-"):
                return False

            neighbors = findNeighbors(i,j)

            current = current + board[i][j]

            if not word.startswith(current):
                return False

            if current == word:
                return True

            orig, board[i][j] = board[i][j], "-"
            for x,y in neighbors:
                if dfs(board, x, y, current):
                    return True

            board[i][j] = orig

            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if dfs(board, r, c, ""):
                    return True

        return False

board =[["a","a","b","a","a","b"],["b","a","b","a","b","b"],["b","a","b","b","b","b"],["a","a","b","a","b","a"],["b","b","a","a","a","b"],["b","b","b","a","b","a"]]
word = "aaaababab"

solver = Solution()
print(solver.exist(board, word))
