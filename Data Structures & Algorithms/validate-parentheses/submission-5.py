from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairing = {")": "(", "}":"{", "]":"["}

        for bracket in s: 
            if bracket in pairing:
                if not stack:
                    return False
                else: 
                    st = stack.pop()

                if pairing[bracket] != st:
                    return False
            else: 
                stack.append(bracket)
        if stack: 
            return False

        return True
                