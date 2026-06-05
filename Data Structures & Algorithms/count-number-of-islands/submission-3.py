class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        
        
        def dfs(x,y):
            if (x,y) in seen or not (0 <= x <len(grid)) or not (0<= y < len(grid[0])):
                return 
            
            if grid[x][y] == "1":
                seen.add((x,y))
                dfs(x+1, y)
                dfs(x, y + 1)
                dfs(x - 1, y)
                dfs(x, y - 1)


        
        
        for x in range(len(grid)): 
            for y in range(len(grid[0])): 
                print("in loop")
                if grid[x][y] == "1" and (x,y) not in seen: 
                    print("in if")
                    islands += 1
                    dfs(x,y)
        
        return islands
    