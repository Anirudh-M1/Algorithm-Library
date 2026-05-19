class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for idx,num in enumerate(nums): 
            if target - num in needed: 
                return [needed[target - num], idx]
            else: 
                if num not in needed: 
                    needed[num] = idx
