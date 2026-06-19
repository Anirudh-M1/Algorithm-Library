class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Planning : BFS 
        #Artificial Level Tracking
        n = len(grid)
        lastPos = (n - 1, n - 1)
        queue = deque()
        elevation = 1

        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], (0,0)))
        visited = set()
        nei = [(1, 0), (0,1), (-1, 0), (0, -1)]
        while (queue or minHeap) and lastPos not in visited:

            while minHeap and minHeap[0][0] <= elevation:
                _, point = heapq.heappop(minHeap)
                queue.append(point)
                if point == lastPos: 
                    return elevation
            # print(f"-- ELEVATION  {elevation} --")
            # print(queue)
            # print(minHeap)
            curLen = len(queue)
            for i in range(curLen):
                (x,y) = queue.popleft()
                
                if (x,y) not in visited: 
                    visited.add((x,y))
                    
                    for dx, dy in nei:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0<= ny <n and (nx, ny) not in visited:
                            heapq.heappush(minHeap, (grid[nx][ny], (nx, ny)))
            
            if curLen == 0: 
                elevation +=1

    
        return elevation
                

    
            
