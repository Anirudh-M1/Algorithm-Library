class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dfs(i, j): 
            if (i, j) in memo: 
                return memo[(i, j)]
            
            if j == len(s) + 1: 
                if i != j: 
                    return False
                else: 
                    return True 
            
            if s[i:j+1] in wordDict: 
                #take or keep moving
                memo[(i,j)] = dfs(j+1, j+1) or dfs(i, j+ 1)
            else: 
                memo[(i,j)] = dfs(i, j+ 1)
            
            return memo[(i,j)]
        
        return dfs(0,0)