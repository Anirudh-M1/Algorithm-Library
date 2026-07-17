class Solution:
    def jump(self, nums: List[int]) -> int:
        
        farthest = 0
        levelStart = 0
        jumps = 0
        while farthest < len(nums) - 1:
            levelEnd = farthest
            for j in range(levelStart, levelEnd + 1):
                farthest = max(farthest, j + nums[j])
            
            levelStart = levelEnd + 1
            jumps += 1 

        return jumps