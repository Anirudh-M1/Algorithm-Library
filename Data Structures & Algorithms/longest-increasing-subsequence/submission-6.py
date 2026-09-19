class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i, largestIdx): 
            if (i, largestIdx) in memo: 
                return memo[(i, largestIdx)]
            if i>=len(nums): 
                return 0 
            
            if largestIdx == -1 or nums[i] > nums[largestIdx]: 
                #take or skip 
                val = max(dfs(i + 1, i) + 1, dfs(i+ 1, largestIdx))
            else: 
                #skip
                val = dfs(i+ 1, largestIdx)

            memo[(i, largestIdx)] = val
            return memo[(i, largestIdx)]
        
        return dfs(0, -1)