from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairing = {")": "(", "}":"{", "]":"["}

        for bracket in s: 
            if bracket in pairing:
                if not stack or pairing[bracket] != stack.pop():
                    return False
            else: 
                stack.append(bracket)
        
        if stack: 
            return False
        else:
            return True
                