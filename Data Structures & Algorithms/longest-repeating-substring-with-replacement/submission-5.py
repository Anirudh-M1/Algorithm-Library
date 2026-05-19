from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0 
        w = defaultdict(int)

        for right in range(len(s)): 
            w[s[right]] += 1 

            if (right-left+1) - max(w.values()) <= k: 
                maxLen = max(maxLen, sum(w.values()))
            else : 
                w[s[left]] -= 1 
                left +=1          
        
        return maxLen
