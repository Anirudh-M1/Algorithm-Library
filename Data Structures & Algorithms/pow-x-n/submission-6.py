class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        while n > 0:
            ans*= x
            n -= 1 
        
 
        while n < 0:
            ans*= 1/x
            n += 1 
        
        return ans

