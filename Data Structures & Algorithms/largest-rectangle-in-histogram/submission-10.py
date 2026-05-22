class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #planning, Monotomic Stack
        #when the value is less, pop it, this gives us a max horizontal rectangle possible
        
        #             # # -> EXTEND
        #         #   # # # -> EXTEND
        #       # # # # # # -> EXTEND
        #       # # # # # # 

        stack = deque() #height, index
        maxRect = 0 
        for i in range(len(heights)): 
            while stack and stack[-1][0] > heights[i]: 
                height, index = stack.pop()
                reachBack = index - stack[-1][1] if stack else index + 1
                #print(f"PROCESSING: considering rect of height {height} at position {index} extended {i -index - 1} spaces spaces with a reachBack of {reachBack}")
                maxRect = max(maxRect, (i - index - 1 + reachBack) * height)
                #print(f"current max {maxRect}")

            stack.append([heights[i], i])


        end = len(heights) - 1 
        while stack: 
            #print(stack)
            height, index  = stack.pop()
            reachBack = index - stack[-1][1] - 1 if stack else index
            #print(f"REACHED END: considering rect of height {height} at position {index} extended {end-index + 1} spaces with a reachBack of {reachBack}")
            maxRect = max(maxRect, (end - index + 1 + reachBack) * height)
            #print(f"current max {maxRect}")

        return maxRect