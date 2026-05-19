class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp: 
                idx = stack.pop()[1]
                ans[idx] = (i - idx)
            stack.append((temp,i))

        return ans
        
