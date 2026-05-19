class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for idx,num in enumerate(nums):
            if num in hm: 
                return  [hm[num], idx]
            print(hm)
            hm[target - num] = idx
        