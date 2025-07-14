class Solution:
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[-1] == amount + 1:
            return -1
        return dp[-1]

solver = Solution()
print(solver.coinChange([5,2,1], 11))
