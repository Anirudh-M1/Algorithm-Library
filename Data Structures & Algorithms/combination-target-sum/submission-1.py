class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(remaining, i):

            if remaining == 0: 
                ans.append(subset.copy())
                return
            elif remaining < 0 or i == len(nums): 
                return
            
            subset.append(nums[i])
            dfs(remaining - nums[i], i)

            subset.pop()
            dfs(remaining ,i + 1)
        
        dfs(target, 0)

        return ans