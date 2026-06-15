class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0: 
            return False
        
        target = total//2
        
        seen = {}
        def dfs(i, t):
            if (i, t) in seen:
                return seen[(i,t)]

            if t < 0:
                return False
                
            if t == 0: 
                return True

            if i == len(nums) and t != 0: 
                return False
            
            
            seen[(i, t)] = dfs(i+1, t - nums[i]) or dfs(i + 1, t)
            return seen[(i, t)] 


        return dfs(0, target)

