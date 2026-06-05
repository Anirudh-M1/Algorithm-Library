class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #PLANNING: start at treasure, use bfs, and update a you go
        queue = deque()
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 0:
                    queue.append([i,j])
    
        distance = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                x , y = queue.popleft()
                
                if not 0<=x<len(grid) or not 0<=y< len(grid[0]): 
                    continue
            
                if grid[x][y] != -1 and (x,y) not in visited:
                    visited.add((x,y))
                    grid[x][y] = min(grid[x][y], distance)
                    queue.append([x + 1, y])
                    queue.append([x, y + 1])
                    queue.append([x - 1, y])
                    queue.append([x, y - 1])
            
            distance += 1

