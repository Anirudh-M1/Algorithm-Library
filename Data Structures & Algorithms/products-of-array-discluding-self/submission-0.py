class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        prod = [1]*n

        for i in range(1,len(nums)): 
            prefix[i] = prefix[i-1]*nums[i-1]

        print(prefix)
        for i in range(len(nums)-2,-1,-1): 
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix)

        for i in range(len(nums)): 
            prod[i] = suffix[i]*prefix[i]
        
        return prod