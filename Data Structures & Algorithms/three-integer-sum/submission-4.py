class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort()
        for i, num in enumerate(nums): 
            if i > 0 and num == nums[i-1]:
                continue          
            vals = self.twoSum(nums, i , - num)
            if vals:
                for val in vals:
                    sols.append(val)
        return list(sols)

    def twoSum(self, nums:List[int] , i:int, target:int) -> List[int]: 
        left, right = i+1, len(nums) -1
        vals = []
        while left < right:     
            curSum = nums[left] + nums[right]
            if curSum < target: 
                left+=1 
            elif curSum > target: 
                right-=1
            else: 
                vals.append([-target, nums[right], nums[left]])
                lv, rv = nums[left], nums[right] 
                while left< right and nums[left] == lv:
                    left+=1
                while left<right and  nums[right] == rv:
                    right-=1

        return vals
            