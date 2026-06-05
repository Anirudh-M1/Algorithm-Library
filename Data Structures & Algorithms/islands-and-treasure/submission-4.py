class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j] == 0: 
                    queue.append((i,j))
    
        
        neighbors = [(1, 0), (0, 1), (-1,0), (0, -1)]
        distance = 1
        
        while queue:
            for _ in range(len(queue)): 
                x,y = queue.popleft()
                
                for nx,ny in neighbors: 
                    if 0<= x+nx< len(grid) and 0<=y+ny<len(grid[0]) and grid[x+nx][y+ny] == 2147483647:
                        grid[x+nx][y+ny] = distance 
                        queue.append((x+nx,y+ny))
        
            distance+=1


