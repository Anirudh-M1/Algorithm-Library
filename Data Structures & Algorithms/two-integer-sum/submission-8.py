class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}

        for idx,num in enumerate(nums):
            if target - num in have: 
                return  [have[target - num], idx]

            have[num] = idx
        