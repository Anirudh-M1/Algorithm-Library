class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(remaining, subset, i):
            print(":::::") 
            print(remaining)
            if remaining == 0: 
                print(f"ans is now {ans}")
                ans.append(subset.copy())
                return
            elif remaining < 0: 
                return
            if i == len(nums): 
                return
            
            subset.append(nums[i])
            print(subset)


            dfs(remaining - nums[i],subset, i)

            subset.pop()
            dfs(remaining,subset ,i + 1)
        
        dfs(target, [], 0)

        return ans