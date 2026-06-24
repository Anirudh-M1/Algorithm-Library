from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i,j): 
            if j == len(p): 
                return i == len(s)

            match = False
            if i < len(s) and (s[i] == p[j] or p[j] == "."): 
                match = True
            
            if j + 1 < len(p) and p[j+1] == "*": 
                use = dfs(i,j + 2) 
                dontUse = match and dfs((i+1), j)
                return use or dontUse

            if match:
                return dfs(i+1, j + 1)
            
            return False
        
        return dfs(0,0)