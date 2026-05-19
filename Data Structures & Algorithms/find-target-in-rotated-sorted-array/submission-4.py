class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        #Input: nums = [3,4,5,6,1,2], target = 1
        while left < right: 
            mid = (left+right)//2
                
            if nums[mid] > nums[right]:
                left = mid + 1 
            elif nums[mid] < nums[right]: 
                right = mid 
        
        pivot = left
        print(pivot)
        if target > nums[len(nums) - 1]:
            return self.binarySearch(0, pivot, nums, target)
        else: 
            return self.binarySearch(pivot, len(nums) - 1 , nums, target)
        
    def binarySearch(self, l, r, array, target): 
        while l <= r: 
            m = (l+r)//2
            if target > array[m]:
                l = m + 1
            elif target < array[m]: 
                r = m - 1
            else:
             return m
        return -1 
            