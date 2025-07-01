from collections import deque


class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        min_rolls = [-1] * (len(board) ** 2 + 1)
        queue = deque()
        min_rolls[1] = 0
        queue.append(1)

        while queue:
            x = queue.popleft()
            for i in range(1, 7):
                t = x + i
                if t > len(board) ** 2:
                    break

                row = (t-1) // n
                col = (t-1) % n
