from collections import deque


class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []

        combinations = []
        letters = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        digits = deque([char for char in digits])

        def dfs(digits, acc):
            nonlocal letters
            nonlocal combinations

            if not digits:
                combinations.append(acc)
                return

            digit = digits.popleft()
            digit_letters = [char for char in letters[digit]]
            for letter in digit_letters:
                dfs(digits, acc + letter)

            digits.appendleft(digit)
            return

        dfs(digits, "")
        return combinations

solver = Solution()
print(solver.letterCombinations(""))
