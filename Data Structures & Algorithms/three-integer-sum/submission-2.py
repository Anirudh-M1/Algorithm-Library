class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = set()
        nums.sort()
        for i, num in enumerate(nums): 
            vals = self.twoSum(nums[:i] + nums[i+1:], 0-num)
            if vals:
                for triplet in vals:
                    sols.add(tuple(sorted(triplet)))
        return list(sols)

    def twoSum(self, nums:List[int] , target) -> List[int]: 
        left, right = 0, len(nums) -1
        vals = []
        while left < right:     
            curSum = nums[left] + nums[right]
            if curSum < target: 
                left+=1 
            elif curSum > target: 
                right-=1
            else: 
                vals.append([-target, nums[right], nums[left]])
                right-=1
                left+=1

        return vals
            