class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s2) < len(s1):
        #     return False


        l = 0 
        s1Profile = Counter(s1)
        s2Profile = Counter(s2[0:len(s1)])
        
        for r in range(len(s1), len(s2), 1): 
            print(r)
            print(f" s1 profile {s1Profile}")
            print(f" window of s2 profile {s2Profile}")
            if s1Profile == s2Profile: 
                return True
            

            s2Profile[s2[l]] -= 1
            s2Profile[s2[r]] += 1
            l+=1


        return s1Profile == s2Profile 
            