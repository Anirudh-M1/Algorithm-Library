class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        best = 0 
        for n in prices[1:]: 
            minSoFar = min(minSoFar, n)

            best = max(best, n - minSoFar)
        
        return best