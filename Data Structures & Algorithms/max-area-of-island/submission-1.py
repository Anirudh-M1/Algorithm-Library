class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        self.maxArea = 0
        def dfs(r,c, area): 
            if r >= rows or r < 0 or c >= cols or c < 0: 
                return 0
            
            if (r,c) not in visited and grid[r][c] == 1:
                visited.add((r,c))
                a1 = dfs(r+1, c, area + 1)
                a2 = dfs(r-1, c,  area + 1)
                a3 = dfs(r, c+1,  area + 1)
                a4 = dfs(r, c-1,  area + 1)
                return a1+a2+a3+a4 + 1
            return 0


            
        for r in range(rows): 
            for c in range(cols): 
                if (r,c) not in visited and grid[r][c] == 1: 
                    self.maxArea = max(dfs(r, c, 0), self.maxArea)

        return self.maxArea
            


