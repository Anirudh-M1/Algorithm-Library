class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Planning : BFS 
        #Artificial Level Tracking
        n = len(grid)
        lastPos = (n - 1, n - 1)
        queue = deque()
        elevation = grid[0][0]
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], (0,0)))
        visited = set()
        visited.add((0,0))

        nei = [(1, 0), (0,1), (-1, 0), (0, -1)]
        while (queue or minHeap):

            while minHeap and minHeap[0][0] <= elevation:
                _, point = heapq.heappop(minHeap)
                queue.append(point)
                if point == lastPos: 
                    return elevation

            curLen = len(queue)
            for i in range(curLen):
                (x,y) = queue.popleft()
                
                for dx, dy in nei:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0<= ny <n and (nx, ny) not in visited:
                        heapq.heappush(minHeap, (grid[nx][ny], (nx, ny)))
                        visited.add((nx, ny))
        
            if curLen == 0 and minHeap: 
                elevation = minHeap[0][0]
    
        return elevation
                

    
            
