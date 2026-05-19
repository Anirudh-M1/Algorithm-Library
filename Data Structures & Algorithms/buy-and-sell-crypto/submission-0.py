class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        mini = prices[buy]
        while buy < len(prices)-1:
            mini = min(mini, prices[buy])
            if mini < prices[buy+1]:
                profit = max(profit, prices[buy+1] - mini)
            buy +=1    
        return profit
