class Solution:
    def robmemo(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i): 
            if i in memo: 
                return memo[i]

            if i >= len(nums): 
                return 0
            
            memo[i] = max(nums[i]+ dfs(i+2), dfs(i + 1))
            return memo[i]
        
        
        return dfs(0)
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+2)

        for i in range(n-1, -1, -1): 
            dp[i] = max(nums[i]+ dp[i+ 2], dp[i + 1])
        
        return dp[0]