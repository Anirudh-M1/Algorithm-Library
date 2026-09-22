class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, target): 
            if (i, target) in memo: 
                return memo[(i, target)]
            
            if i == len(nums): 
                return target == 0 
            
            memo[(i, target)] = dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])

            return memo[(i, target)]

        return dfs(0, target)