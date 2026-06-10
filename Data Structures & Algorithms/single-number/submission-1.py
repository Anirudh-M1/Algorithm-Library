class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Planning: XOR is perfect, a ^ a = 0, a ^ 0 = a
        
        res = 0
        for num in nums: 
            res = res ^ num
    
        return res 