class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curSum = 0
        for num in nums: 
            if curSum<0: 
                curSum = 0
            curSum += num
            maximum = max(curSum, maximum)

        return maximum