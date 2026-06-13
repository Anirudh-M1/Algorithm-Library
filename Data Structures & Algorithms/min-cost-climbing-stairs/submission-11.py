class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Top down cache         
        minCosts =  {}
        def dfs(n): 
            if n in minCosts:
                return minCosts[n]
            if n >= len(cost):
                return 0

            minCosts[n] = min(dfs(n +1), dfs(n+2)) + cost[n]
            return minCosts[n]

        return min(dfs(1), dfs(0))