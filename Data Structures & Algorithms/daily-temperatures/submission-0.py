class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            print(stack) 
            if not stack or temp<= stack[-1][0]:
                stack.append((temp,i))
            else:
                while stack: 
                    if stack[-1][0] < temp:
                        idx = stack.pop()[1]
                        ans[idx] = (i - idx)
                        print(ans)
                    else:
                        break
                stack.append((temp,i))

        return ans
        
