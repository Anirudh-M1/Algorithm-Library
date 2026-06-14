class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {}
        def dfs(i): 
            if i in cache: 
                return cache[i]
            if i == len(s): 
                return 1
            if i > len(s): 
                return 0

            count = 0
            if i + 2 <= len(s) and (s[i]  == "1" or (s[i] == "2" and s[i+1] in "0123456")): 
                count += dfs(i + 2)
            
            if s[i] != "0": 
                count += dfs(i+1)

            cache[i] = count
            return count
        
        return dfs(0)