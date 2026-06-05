class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            if not 0<=x<len(grid) or not 0 <= y < len(grid[0]): 
                return 0
            
            if grid[x][y] == 1:
                grid[x][y] = 0

                return (1 
                + dfs(x+1,y)
                + dfs(x,y+1)
                + dfs(x-1,y)
                + dfs(x,y-1))
            
            return 0
            
        maxArea = 0
        for x in range(len(grid)): 
            for y in range(len(grid[0])): 
                if grid[x][y] == 1: 
                    maxArea = max(maxArea,dfs(x,y))
    
        return maxArea
