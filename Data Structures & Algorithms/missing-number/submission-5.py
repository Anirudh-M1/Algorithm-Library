class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        nums.sort()
        print(nums)
        while l<=r:
            mid = (l + r)//2
            if nums[mid] > mid:
                r = mid - 1
            
            elif nums[mid] == mid:
                l = mid + 1

        return l
        