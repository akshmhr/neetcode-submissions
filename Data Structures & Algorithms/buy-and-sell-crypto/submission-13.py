class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < Min:
                Min = prices[i] 


            profit = max(profit, prices[i] - Min)

        return profit