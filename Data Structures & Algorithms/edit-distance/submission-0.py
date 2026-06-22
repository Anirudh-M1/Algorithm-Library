from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        @cache
        def dfs(i, j):

            if i >= len(word1) or j >= len(word2): 
                return max(len(word1) - i,len(word2 ) - j)
            #match
            if word1[i]== word2[j]: 
                return dfs(i + 1, j + 1)

            else: #3 ways to fix

                #insert into w1
                insert = dfs(i, j + 1) + 1
                #delete from w1
                delete = dfs(i + 1, j) + 1
                #replace in w1 
                replace = dfs(i + 1, j + 1) + 1

                return min(insert, delete, replace)
            

        return dfs(0, 0)