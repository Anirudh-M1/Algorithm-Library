class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        subset = []

        nums.sort()
        
        def dfs(i): 
            if i == len(nums): 
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
            
            dfs(j)
        
        dfs(0)
        return ans