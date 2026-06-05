class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        countFresh = 0
        for x in range(len(grid)): 
            for y in range(len(grid[0])):
                if(grid[x][y]) == 2:
                    queue.append((x,y)) 
                elif(grid[x][y]) == 1: 
                    countFresh +=1 
        
        time = 0
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while queue:
            rottedThisRound = False
            
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for r,c in neighbors:
                    nx,ny = x+r, y+c

                    if (0<=nx<len(grid)) and (0<=ny<len(grid[0])) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        countFresh -= 1
                        queue.append((nx,ny))
                        rottedThisRound = True

                if countFresh == 0: 
                    break
    
            if rottedThisRound: 
                time+=1
        return time  if countFresh == 0 else -1 