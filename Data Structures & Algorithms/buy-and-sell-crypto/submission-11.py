class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        best = 0 
        for n in prices[1:]: 
            best = max(best, n - minSoFar)
            minSoFar = min(minSoFar, n)
        
        return best