from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        ans = []

        @cache
        def dfs(i, j): 
            best = 1
            for di,dj in directions:
                ni, nj = di + i, dj + j 
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                    if matrix[i][j] < matrix [ni][nj]: 
                        best = max(best,1 + dfs(ni, nj)) 
            return best 

        maxval = 0
        for x in range(len(matrix)): 
            for y in range(len(matrix[0])):
                maxval = max(dfs(x,y), maxval)
        return maxval