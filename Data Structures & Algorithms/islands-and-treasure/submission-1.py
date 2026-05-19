class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        ans = [[-1 for _ in range(cols)] for _ in range(rows)] 
        print(ans)


        def bfs(r,c):
            visited = set()
            queue = deque()

            dist = 0
            queue.append((r,c))
            while queue: 
                print(dist)

                for i in range(len(queue)): 
                    r, c = queue.popleft()

                    if r>=rows or r < 0 or c >= cols or c < 0: 
                        continue
                    if (r,c) in visited or grid[r][c] == -1:
                        continue
                    
                    if grid[r][c] == 0:
                        return dist

                    visited.add((r,c))
                    if grid[r][c] == 2147483647: 
                        queue.append((r+1,c))
                        queue.append((r - 1,c))
                        queue.append((r,c+1))
                        queue.append((r,c-1))
                dist+=1 
            
            return -1


        for row in range(rows): 
            for col in range(cols): 
                print(f"finding nearest from ({row},{col})")
                
                ans[row][col] = bfs(row,col)

        for r in range(rows): 
            for c in range(cols): 
                grid[r][c] = ans[r][c]

