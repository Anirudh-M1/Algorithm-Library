class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        prod = [1]*n
        
        prefix = 1 
        for i in range(1,len(nums)): 
            prefix = prefix *nums[i-1]
            prod[i] = prefix

        suffix = 1
        for i in range(len(nums)-2,-1,-1): 
            suffix = suffix * nums[i+1]
            prod[i] = prod[i]*suffix
        
        return prod

