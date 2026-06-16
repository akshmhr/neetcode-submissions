class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        left = 0 

        for right in range(1, n):
            current = (prices[right] - prices[left])
            profit = max(profit, current)
            while (prices[left] > prices[right]) and (left<right):
                left +=1
        return profit