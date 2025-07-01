class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        profit = 0
        current_stock = prices[0]

        for price in prices:
            if price > current_stock:
                profit += price - current_stock

            current_stock = price

        return profit
