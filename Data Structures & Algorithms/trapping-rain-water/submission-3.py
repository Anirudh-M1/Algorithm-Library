class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        water = 0 
        maxLeft = maxRight = 0 
        while left <= right:            
            if height[left]<height[right]:
                maxLeft = max(height[left], maxLeft)
                water += maxLeft- height[left]
                left+=1
            else: 
                maxRight = max(height[right], maxRight)
                water += maxRight - height[right]
                right-=1

        return water