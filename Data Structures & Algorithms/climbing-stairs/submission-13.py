class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
            
        oneBack = 1
        twoBack = 1
        current = 0
        for i in range(n-1): 
            current = oneBack+ twoBack
            
            twoBack = oneBack
            oneBack = current
    
        
        return current