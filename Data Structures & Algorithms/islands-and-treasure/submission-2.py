class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)] 
        print(ans)


        def bfs():
            visited = set()
            queue = deque()
            for r in range(rows): 
                for c in range(cols):
                    if grid[r][c] == 0: 
                        queue.append((r,c))

            dist = 0
            while queue: 
                print(dist)
                for i in range(len(queue)): 
                    r, c = queue.popleft()

                    if r>=rows or r < 0 or c >= cols or c < 0: 
                        continue
                    if (r,c) in visited or grid[r][c] == -1:
                        continue
                    
                    grid[r][c]= dist

                    visited.add((r,c))
                    queue.append((r+1,c))
                    queue.append((r - 1,c))
                    queue.append((r,c+1))
                    queue.append((r,c-1))
                dist+=1 
            
        bfs()
        
                


