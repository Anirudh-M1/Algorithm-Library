class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        next2 = 0
        next1 = cost[-1]
        ans = 0
        for i in range(len(cost) - 2, -1, -1): 
            ans = min(next2, next1) + cost[i]

            next2 = next1
            next1 = ans

        return min(next2, next1)
