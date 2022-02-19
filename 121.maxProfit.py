class Solution:
    def maxProfit(self, prices: list) -> int:
        minPrice = prices[0]
        profit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)
        return 0 if profit < 0 else profit