class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}

        def dp(n): 
            if n > len(cost):
                return float("inf")
            if n == len(cost): 
                return 0

            if n in self.memo: 
                return self.memo[n]

            self.memo[n] = cost[n] + min(dp(n+2), dp(n+1))
            return self.memo[n]


        return min(dp(0),dp(1))