from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        @cache
        def dfs(n): 
            if n == 0: 
                return 1
            if n < 0:
                return 0

            return dfs(n -2) + dfs(n-1)

        return dfs(n)