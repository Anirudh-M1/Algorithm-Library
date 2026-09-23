class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        memo = {}
        def dfs(si, ti): 
            if (si, ti) in memo: 
                return memo[(si, ti)]
            if si == len(s): 
                return 1 if ti == len(t) else 0 
            if ti == len(t): 
                return 1
            if s[si] == t[ti]: 
                # take or skip
                memo[(si, ti)] = dfs(si+ 1, ti +1) + dfs(si+1, ti)
            else: 
                memo[(si, ti)] = dfs(si+1, ti)
            
            return memo[(si, ti)]
        
        return dfs(0, 0)

                
                
            
            
