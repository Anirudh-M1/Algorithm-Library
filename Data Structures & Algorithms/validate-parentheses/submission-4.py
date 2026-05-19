from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for bracket in s: 
            if bracket == "}" or bracket == ")" or bracket == "]":
                
                if not stack:
                    return False
                else: 
                    s = stack.pop()

                if bracket  == "}" and s != "{":
                    return False
                if bracket  == ")" and s != "(":
                    return False
                if bracket  == "]" and s != "[":
                    return False
            else: 
                stack.append(bracket)
        if stack: 
            return False

        return True
                