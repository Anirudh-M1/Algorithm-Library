class Solution:
    def numDecodings(self, s: str) -> int:
        #bottom up approach
        if s[0] == "0": 
            return 0
        
        ways = [0] * (len(s) + 1)
        ways[len(s)] = 1
        for i in range(len(s) - 1, -1, -1): 
            if s[i] == "0": 
                ways[i] = 0 
            else:
                ways[i] = ways[i+1] 

                if i + 1 < len(s) and (s[i] == "1" or (s[i] =="2" and s[i+1] in "0123456")): 
                    ways[i]+= ways[i+2]
        
        return ways[0]