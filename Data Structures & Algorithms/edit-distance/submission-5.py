class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo: 
                return memo[(i,j)]

            if i == len(word1) or j == len(word2): 
                return len(word1)-i + len(word2)-j

            
            if word1[i] == word2[j]: 
                memo[(i, j)] = dfs(i+ 1, j + 1)
            
            else:
            # insert, delete, replace
                memo[(i, j)] = min(dfs(i + 1, j)+ 1, dfs(i, j + 1)+ 1,dfs(i+ 1, j + 1)+ 1)

            return memo[(i, j)]
        
        return dfs(0, 0)