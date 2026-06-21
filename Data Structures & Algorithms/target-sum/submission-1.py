class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i, cur):
            if (i,cur) in memo:
                return memo[(i,cur)]
            if i >= len(nums) and cur == target:
                return 1 
            if i >= len(nums) and cur != target:
                return 0
            
            ways = 0 
            ways += dfs(i+1, cur-nums[i])
            ways += dfs(i+1, cur+nums[i])
            memo[(i,cur)] = ways
            return ways

        return dfs(0,0)