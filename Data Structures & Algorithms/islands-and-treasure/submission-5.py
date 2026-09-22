class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()

        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                if grid[r][c] == 0: 
                    queue.append((r,c))
                    visited.add((r,c))

        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        level = 0 
        while queue: 
            level += 1
            for i in range(len(queue)): 
                r,c = queue.popleft()

                for dr, dc in DIRS: 
                    nr, nc = dr+ r, dc + c

                    if 0<= nr < len(grid) and 0 <= nc < len(grid[0]): 
                        if (nr, nc) not in visited and grid[nr][nc] != -1: 
                            visited.add((nr,nc))
                            grid[nr][nc] = level
                            queue.append((nr,nc))

        