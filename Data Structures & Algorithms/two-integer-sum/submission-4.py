class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sortedNums = sorted(nums)

        left, right = 0, len(nums) - 1
        while left < right: 
            if sortedNums[left] + sortedNums[right] > target: 
                right -=1
            elif sortedNums[left] + sortedNums[right] < target: 
                left +=1 
            else:
                leftIndex = nums.index(sortedNums[left]) 
                nums[leftIndex] = float("-inf")
                rightIndex = nums.index(sortedNums[right])
                return [min(leftIndex, rightIndex),max(leftIndex, rightIndex)]