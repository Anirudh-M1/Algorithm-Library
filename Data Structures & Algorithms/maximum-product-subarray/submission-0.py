class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = 1 
        minVal = 1
        res = nums[0]
        for n in nums:
            temp = maxVal*n 
            maxVal = max(temp, n*minVal, n)
            minVal = min(temp, n*minVal, n)
            res = max(res, maxVal)
        
        return res