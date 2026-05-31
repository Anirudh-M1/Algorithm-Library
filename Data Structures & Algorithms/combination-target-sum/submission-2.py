class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def dfs (i, t):
            if t == 0: 
                ans.append(subset.copy())
                return
            elif t < 0 or i >= len(nums):
                return
            
            subset.append(nums[i])
            
            dfs(i, t - nums[i])

            subset.pop()
            dfs(i + 1, t)
            
        dfs(0, target)

        return ans 

            
        