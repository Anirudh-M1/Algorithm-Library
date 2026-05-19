class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0 
        w = defaultdict(int)
        for right in range(len(s)): 
            w[s[right]] += 1 

            if sum(w.values()) - max(w.values()) <= k: 
                print(sum(w.values()) - max(w.values()))
                print(f"maxFreq in window: {max(w.values())}")
                print(f"current Array: {s[left:right]}")
                maxLen = max(maxLen, sum(w.values()))
            else : 
                if w[s[left]] >= 1:
                    w[s[left]] -= 1 
                    left +=1
                    print(w)
                
        
        return maxLen
