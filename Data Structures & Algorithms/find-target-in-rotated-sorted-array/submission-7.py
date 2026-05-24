class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums)-1
        m = 0
        while l < r: 
            m = (l + r)//2

            if nums[m] <= nums[r]: 
                r = m
            elif nums[m]> m: 
                l = m + 1

        if target <= nums[-1]: 
            return self.binarySearch(l, len(nums) - 1, target, nums)
        else: 
            return self.binarySearch(0, l - 1, target, nums)

    def binarySearch(self, left, right, target, nums): 
        while left<=right: 
            mid = (left + right)//2

            if nums[mid] < target: 
                left = mid + 1
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                return mid 

        return -1