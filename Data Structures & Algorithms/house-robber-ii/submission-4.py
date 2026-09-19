class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:])) 
        
        
    def helper(self, arr): 
        n = len(arr)
        dp = [0]*(n + 2)

        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+2]+ arr[i], dp[i+ 1])
        
        return dp[0]
    


