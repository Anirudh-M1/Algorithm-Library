class Solution:
    def rob(self, nums: List[int]) -> int:
        #top down and cache

        seen = {}
        def dfs(i):
            if i in seen:
                return seen[i] 
            if i >= len(nums):
                return 0
            rob = dfs(i+2) + nums[i] 
            skip = dfs(i+1)

            seen[i] = max(rob, skip)

            return seen[i]

        return dfs(0)