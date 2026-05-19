class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        water = 0 
        maxLeft = maxRight = 0 
        while left <= right: 
            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)
            
            if height[left]<height[right]:
                water += max(0 , min(maxRight,maxLeft) - height[left])
                left+=1
            else: 
                water += max(0, min(maxRight,maxLeft) - height[right])
                right-=1

        return water