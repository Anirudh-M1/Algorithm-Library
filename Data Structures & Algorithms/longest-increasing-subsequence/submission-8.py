class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i, largest): 
            if (i,largest) in memo: 
                return memo[(i,largest)]
            if i == len(nums): 
                return 0
            
            if nums[i] > largest:
                memo[(i,largest)] = max(dfs(i + 1, nums[i]) + 1, dfs(i+1, largest))
            else: 
                memo[(i,largest)] = dfs(i + 1, largest)
            
            return memo[(i,largest)]
        
        return dfs(0, float('-inf'))