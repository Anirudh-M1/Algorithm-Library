class Solution:
    def climbStairs(self, n: int) -> int:
        
        arr = [0] * (n+1)

        def dfs(num):
            if arr[num]: 
                return arr[num]

            if num < 0:
                return 0
            if num == 0:
                return 1

            arr[num] =  dfs(num - 1) + dfs(num - 2)

            return arr[num]
           
        return dfs(n)