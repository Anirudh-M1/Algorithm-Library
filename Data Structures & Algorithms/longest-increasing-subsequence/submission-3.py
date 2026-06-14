class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seen = {}
        def dfs(i, prev):
            if (i,prev) in seen: 
                return seen[(i,prev)]

            if i == len(nums): 
                return 0
            
            take = 0
            if prev < nums[i]: 
                take = dfs(i+1, nums[i]) + 1

            skip = dfs(i+1,prev)
        
            seen[(i,prev)] = max(take, skip)
            return seen[(i,prev)]

        return dfs(0, float("-inf"))

        
            