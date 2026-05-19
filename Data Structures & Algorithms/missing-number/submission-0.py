class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        current = 0
        for i, num in enumerate(nums):
            target += i + 1
            current+= num
        
        return target - current
