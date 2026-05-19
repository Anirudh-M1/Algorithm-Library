class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0

        seenChars = set()

        for right in range(len(s)): 
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left+=1 
        
            seenChars.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen