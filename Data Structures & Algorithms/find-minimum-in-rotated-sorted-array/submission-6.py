class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the elements after the higest are guarenteed to 
        # be lower than the lowest of the left chunk
                  #
                # #
              # # #
              # # #   #      
              # # # # #

              #
              #       #
              #     # #
              #   # # #
              # # # # #
        l, r = 0, len(nums) - 1

        while l <=r: 
            print(nums[l:r+1])
            m = int((l + r)/2) 

            if nums[m] > nums[r]: 
                l = m + 1
            elif nums[m] < nums[r]: 
                r = m 
            elif l == r: 
                return nums[r]
        return nums[r]


