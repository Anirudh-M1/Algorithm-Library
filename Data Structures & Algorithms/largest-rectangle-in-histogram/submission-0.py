class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0 
        for i, height in enumerate(heights): 
            start = i
            while stack and height<stack[-1][0]: 
                bar = stack.pop()
                maxArea= max(maxArea, bar[0] * (i - bar[1]))
                start = bar[1]
            stack.append((height,start))
        
        for bar in stack:
            maxArea= max(maxArea, bar[0] * (len(heights) - bar[1]))

        return maxArea