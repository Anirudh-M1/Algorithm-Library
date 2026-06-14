class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set()
        for word in wordDict:
            words.add(word)

        possibleIdx = {}
        def dfs(i): 
            if i in possibleIdx:
                return possibleIdx[i]

            if i == len(s): 
                return True

            possible = False
            for j in range(i,len(s)): 
                if s[i:j+1] in words: 
                    if dfs(j+1): 
                        possible = True
            
            possibleIdx[i] = possible 
            return possible
        
        return dfs(0)