class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0 
        while n > 0: 
            i+= n % 2
            n = n//2

        return i
        

        