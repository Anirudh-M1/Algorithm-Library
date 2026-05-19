class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = set()
        nums.sort()
        for i, num in enumerate(nums): 
            vals = self.twoSum(nums, i , 0-num)
            if vals:
                for triplet in vals:
                    sols.add(tuple(sorted(triplet)))
        return list(sols)

    def twoSum(self, nums:List[int] , i:int, target:int) -> List[int]: 
        left, right = 0, len(nums) -1
        vals = []
        while left < right:     
            curSum = nums[left] + nums[right]
            if curSum < target or i == left: 
                left+=1 
            elif curSum > target or i == right: 
                right-=1
            else: 
                vals.append([-target, nums[right], nums[left]])
                right-=1
                left+=1

        return vals
            