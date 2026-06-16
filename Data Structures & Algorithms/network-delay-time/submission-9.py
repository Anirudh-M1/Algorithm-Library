class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #PLANNING

        # 1 Hashmaps, node -> (neighbor, time) 

        # BFS with round artificial counting 
                # visited tracking

        # min heap arrival time, node
        #current time goes up, 


        # fill node -> neighbor Hashmap: 
        neighbors = defaultdict(list)
        for s, d, t in times:
            neighbors[s].append((d,t))
        
        queue = deque()
        queue.append(k)
        visited = set()
        minheap = []
        elapsed = 0
        while (queue or minheap) and len(visited) != n :
                
            while minheap and minheap[0][0] <= elapsed:
                time, dest = heapq.heappop(minheap)                
                queue.append(dest)

            for _ in range(len(queue)):
                if queue and queue[0] in visited:
                    queue.popleft()
                elif queue:
                    s = queue.popleft()
                    visited.add(s)
                    if len(visited) == n:
                        return elapsed
                    if s not in neighbors:
                        continue
                    
                    for d, t in neighbors[s]:
                        if d not in visited:
                            heapq.heappush(minheap, (t+elapsed ,d))

        
            elapsed +=1
        
        return -1
        



