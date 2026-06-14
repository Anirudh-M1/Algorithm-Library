class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possible = [False] * (len(s) + 1)
        possible[len(s)] = True 

        for i in range(len(s)-1 , -1, -1): 
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w: 
                    possible[i] = possible[i + len(w)]
                
                if possible[i]: 
                    break
        
        return possible[0]