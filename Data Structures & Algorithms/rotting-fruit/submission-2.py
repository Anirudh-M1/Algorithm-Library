class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.minute = 0
        self.needed = 0
        visited = set()
        queue = deque()

        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1: 
                    self.needed +=1

        def bfs(): 

            while queue and self.needed > 0: 
                self.minute +=1
                for i in range(rows): 
                    print(grid[i])

                for i in range(len(queue)):
                    
                    r,c = queue.popleft()

                    if r < 0 or r >= rows or c < 0 or c >= cols: 
                        continue
                    
                    if grid[r][c] == 0:
                        continue

                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            self.needed -= 1
                            queue.append((nr, nc))

                
        bfs()

        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == 1: 
                    return -1

        return self.minute
             
