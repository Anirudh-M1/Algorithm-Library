from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): 
            return False
        @cache
        def dfs(i, j):

            if  i >= len(s1) and j >= len(s2):
                return True 
            if i >= len(s1):
                print(f"Remaining S: {s3[i + j:]} Remaining s2 {s2[j:]}")
                return s3[i + j:] == s2[j:]

            if j >= len(s2): 
                print(f"Remaining S: {s3[i  + j:]} Remaining s1 {s1[i:]}")

                return s3[i+j:] == s1[i:]

            if s1[i] == s3[i+j]: 
                if dfs(i + 1, j): 
                    return True
                
            if s2[j] == s3[i+j]: 
                if dfs(i, j + 1): 
                    return True


            return False
            
        return dfs(0, 0)
