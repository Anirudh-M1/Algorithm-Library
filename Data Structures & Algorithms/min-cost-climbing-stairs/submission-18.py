from functools import cache
class Solution:
    def minCostClimbingStairsMemo(self, cost: List[int]) -> int:
        
        @cache 
        def dfs(i): 
            if i == len(cost): 
                return 0
            if i > len(cost): 
                return float("inf")
            
            return min(dfs(i+2), dfs(i+1)) + cost[i]
        
        return min(dfs(0), dfs(1)) 

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)
        for i in range(n-1, -1, -1): 
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        
        return min(dp[0],dp[1])


