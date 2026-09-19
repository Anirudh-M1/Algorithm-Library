class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0 ,  len(heights) - 1
        maxLeft, maxRight = 0, 0

        water = 0

        while left < right: 
            if heights[left] < heights[right]: 
                maxLeft = max(maxLeft, heights[left])
                water+= maxLeft - heights[left]
                left += 1
            else: 
                maxRight = max(maxRight, heights[right])
                water+= maxRight - heights[right]
                right -= 1
        
        return water


