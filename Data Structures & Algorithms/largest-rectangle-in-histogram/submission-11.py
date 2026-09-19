class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = heights + [0]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i 
            while stack and h <= stack[-1][0]:
                pH, pS = stack.pop()
                maxArea = max(maxArea, pH * (i - pS))
                start = pS


            stack.append((h, start))
        
        return maxArea
