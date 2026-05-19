class Solution:
    from collections import defaultdict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLeft = 0
        r = windowLeft + len(s1)
        s1Profile = Counter(s1)
        windowProfile = defaultdict(int)
        for windowRight in range(len(s2)): 
            windowProfile[s2[windowRight]] +=1

            
            if windowProfile == s1Profile:
                return True

            if windowRight - windowLeft + 1 >= len(s1): 
                windowProfile[s2[windowLeft]] -=1
                if windowProfile[s2[windowLeft]] == 0: 
                    del windowProfile[s2[windowLeft]]
                windowLeft += 1
            
        return False