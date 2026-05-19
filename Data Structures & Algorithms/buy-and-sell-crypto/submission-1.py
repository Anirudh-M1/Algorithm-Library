class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        mini = prices[buy]
        while buy < len(prices):
            mini = min(mini, prices[buy])
            profit = max(profit, prices[buy] - mini)
            buy +=1    
        return profit
