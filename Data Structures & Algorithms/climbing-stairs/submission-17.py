class Solution:
    def climbStairs(self, n: int) -> int:
     
        seen = {}
        seen[0] = 1
        seen[1] = 1
        for i in range(2,n +1): 
            seen[i] = seen[i-1] + seen[i-2]
        
        return seen[n]
       