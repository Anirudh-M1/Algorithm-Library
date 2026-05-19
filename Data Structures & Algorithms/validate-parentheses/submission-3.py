from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        n = len(s)
        if n % 2!= 0: 
            return False

        for bracket in s: 
            if bracket == "}" or bracket == ")" or bracket == "]":
                if not stack:
                    return False
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
                