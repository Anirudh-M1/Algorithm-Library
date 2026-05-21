class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contained = set()
        l = 0
        res = 0


        for i in range(len(s)): 
            while s[i] in contained: 
                contained.remove(s[l])
                l = l+1
            
            contained.add(s[i])
            res = max(res, i - l + 1)
            print(contained)
        
        return res