class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Top down cache         
        minCosts =  {}
        def dfs(n, currentCost): 
            if n in minCosts:
                return minCosts[n]
            if n >= len(cost):
                return currentCost

            minCosts[n] = min(dfs(n +1, 0), dfs(n+2, currentCost)) + cost[n]
            return minCosts[n]

        return min(dfs(1, 0), dfs(0, 0))