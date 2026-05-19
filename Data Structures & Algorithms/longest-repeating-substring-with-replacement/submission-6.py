from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0 
        w = defaultdict(int)

        for right in range(len(s)): 
            w[s[right]] += 1 
                
            while right-left+1 - max(w.values()) > k: 
                w[s[left]] -= 1 
                left +=1          
            maxLen = max(maxLen, sum(w.values()))
        return maxLen
