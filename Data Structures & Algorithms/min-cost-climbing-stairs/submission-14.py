class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom up
        seen = {}
        seen[len(cost)] = 0
        seen[len(cost) -1] = cost[len(cost) -1]
        for i in range(len(cost) - 2, -1 , -1):
            seen[i] = min(seen[i+2], seen[i+1]) + cost[i] 
        

        return min(seen[0], seen[1])