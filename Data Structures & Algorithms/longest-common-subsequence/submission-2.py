class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        seen = {}

        def dfs(i, j): 
            if (i,j) in seen:
                return seen[(i,j)]

            if i>= len(text1) or j >= len(text2): 
                return 0 

            
            if text1[i] == text2[j]: 
                seen[(i,j)] = dfs(i + 1, j + 1) + 1 

            else: 
                seen[(i,j)] =  max(dfs(i + 1, j), dfs(i, j+ 1))
            
            return seen[(i,j)] 

        return dfs(0,0)

    