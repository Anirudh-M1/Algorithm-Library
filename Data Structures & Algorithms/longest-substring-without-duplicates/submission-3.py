class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1: 
            return len(s)

        left, right = 0, 1
        window = set()
        maxLen = 1
        window.add(s[left])
        while right < len(s): 
            if s[right] in window:
                print("****")
                maxLen = max(maxLen, (right- left))
                print(maxLen)
                print(f"left: {left}, right: {right}")
                
                while s[left]!= s[right]:
                    window.remove(s[left])
                    left+=1
                window.remove(s[left])
                left+=1
                
            window.add(s[right])
            right +=1
        print(window)
        maxLen = max(maxLen, (right- left))
        return maxLen
            