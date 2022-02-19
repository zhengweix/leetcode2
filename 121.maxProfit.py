class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        minPrice = prices[0]
        profit = 0
        for i in range(n-1):
            if prices[i] >= prices[i+1]:
                minPrice = min(minPrice, prices[i+1])
            else:
                if profit < prices[i+1] - minPrice:
                    profit = prices[i+1] - minPrice
        return 0 if profit < 0 else profit



S = Solution()
print(S.maxProfit([7,1,5,3,6,4]))