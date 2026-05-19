class Solution:
    from collections import deque 
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ocean ------> higher 
        rows = len(heights)
        cols = len(heights[0])

        def bfs(queue, visited): 
            
            while queue: 
                r, c = queue.pop()
        
                
                neighbors = [(r, c + 1), (r, c-1), (r+1, c), (r-1, c)]
                
                for nr, nc in neighbors:    
                    if 0 <= nr < rows and 0 <= nc < cols: 
                        if heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited: 
                            visited.add((nr,nc))
                            queue.append((nr,nc))


            return visited
    
        atlanticQueue = deque()
        pasificQueue = deque()
        atlanticBase = set()
        pasificBase = set()
        for i in range(rows): 
            for j in range(cols):  
                if i == 0: 
                    pasificQueue.append((i,j))
                    pasificBase.add((i,j))
                if j == 0: 
                    pasificQueue.append((i,j))
                    pasificBase.add((i,j))

                if i == rows - 1: 
                    atlanticQueue.append((i,j))
                    atlanticBase.add((i,j))
                if j == cols - 1: 
                    print((i,j))
                    atlanticQueue.append((i,j))
                    atlanticBase.add((i,j))



        bfs(atlanticQueue, atlanticBase)
        bfs(pasificQueue, pasificBase)

        ans = []
        for a in atlanticBase: 
            if a in pasificBase: 
                ans.append(list(a))

        print(ans)
        return ans    