class Solution:
    def checkValidString(self, s: str) -> bool:
         #planning: if negative immediately use buffer
         # if positive wait till end and check if total buffer can accomodate

        starStack = []
        openStack = []
        for i, p in enumerate(s): 
            if p == "(": 
                openStack.append(i)
            elif p == ")": 
                if openStack:
                    openStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
            else:
                starStack.append(i)

        while openStack and starStack:
            if openStack[-1] > starStack[-1]: 
                return False
            openStack.pop()
            starStack.pop()
            
        return len(openStack) == 0