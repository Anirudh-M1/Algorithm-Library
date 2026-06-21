class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # PLANNING: bfs, artifical level tracking
        adj = defaultdict(list)
        for i in range(len(flights)): 
            f, t, c = flights[i]
            adj[f].append((t, c))


        queue = deque()
        queue.append((src, 0))
        count = 0 
        destCost = float("inf")
        minCost = [float("inf")] * n 
        #bfs
        while queue and count <= k:

            for _ in range(len(queue)): 
                s, csf = queue.popleft()
                
                for t, c in adj[s]: 
                    if t == dst: 
                        destCost = min(destCost, csf + c)
                    if csf+c < minCost[t]:
                        queue.append((t, csf +c))
                        minCost[t] = csf+c 

            count +=1


        return destCost if destCost != float("inf") else -1
