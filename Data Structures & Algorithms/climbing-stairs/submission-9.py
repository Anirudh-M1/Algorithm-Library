class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        seen = {}
        def dfs(n): 
            if n in seen: 
                return seen[n]
            
            if n == 0:
                return 1
            if n < 0:
                return 0

            seen[n] = dfs(n -2) + dfs(n-1)
            return seen[n]

        return dfs(n)