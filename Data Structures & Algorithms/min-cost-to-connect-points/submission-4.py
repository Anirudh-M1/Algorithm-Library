class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        frontier = []
        for i, p in enumerate(points): 
            points[i] = tuple(p)

        def addEdges(p1, heap):
            for p2 in points:
                p2  = p2
                if p2 != p1 and p2 not in visited:
                    heapq.heappush(frontier, (self.manhattanDist(p1, p2), p2))

        visited = set()
        visited.add(points[0])
        addEdges(points[0], frontier)
        cost = 0
        while len(visited)!= len(points):
            dist, point = heapq.heappop(frontier)
            if point not in visited:
                visited.add(point)
                cost += dist
                addEdges(point, frontier)

        return cost
    def manhattanDist(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        return abs(x1 - x2) + abs(y1 - y2)