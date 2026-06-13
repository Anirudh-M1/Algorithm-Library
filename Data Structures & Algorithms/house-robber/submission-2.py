class Solution:
    def rob(self, nums: List[int]) -> int:
        #top down and cache

        seen = {}
        def dfs(i):
            if i in seen:
                return seen[i] 
            if i >= len(nums):
                return 0

            seen[i] = max(dfs(i+2), dfs(i+3)) + nums[i]
            return seen[i]

        return max(dfs(0), dfs(1))