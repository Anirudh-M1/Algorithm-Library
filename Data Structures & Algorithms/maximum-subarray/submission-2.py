class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float("-inf")
        for num in nums:
            curSum += num
            maxSum = max(curSum, maxSum)                
            curSum = max(curSum,0)
        

        return maxSum