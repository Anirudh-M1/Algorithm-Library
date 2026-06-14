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
            print(s[i])
            if i + 2 <= len(s) and int(s[i:i + 2]) <= 26 and s[i] != "0": 
                count += dfs(i + 2)
            
            if s[i] != "0": 
                count += dfs(i+1)

            cache[i] = count
            return count
        
        return dfs(0)