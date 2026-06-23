from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s): 
            return 0

        @cache
        def dfs(si, ti): 
            if ti == len(t): 
                return 1
            
            if si == len(s) and ti < len(t): 
                return 0

            take, skip, nxt = 0,0,0 
            if s[si] == t[ti]:
                # if same 
                #take
                take = dfs(si + 1, ti + 1)
                #skip
                skip = dfs(si + 1, ti)
            else: 
                nxt = dfs(si+ 1, ti)
            
            return take + skip+ nxt    
        
        return dfs(0, 0)