class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIdx, rightIdx = 0, len(nums) - 1 
        
        while leftIdx <= rightIdx:
            mid = (leftIdx+rightIdx)//2

            if target > nums[mid]: 
                leftIdx = mid + 1
            elif target < nums[mid]: 
                rightIdx = mid - 1
            else: 
                return mid
            
        return -1

