class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = {}
        pairs["{"] = "}"
        pairs["("] = ")"
        pairs["["] = "]"

        for p in s:
            if p in pairs: 
                stack.append(p)
            elif stack and p == pairs[stack[-1]]: 
                stack.pop()
            else: 
                return False
        
        return len(stack) == 0
