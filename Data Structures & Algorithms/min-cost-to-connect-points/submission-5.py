class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minDist = [float("inf")] * len(points)
        visited = set()

        minDist[0] = 0
        cost = 0

        while len(visited) != len(points): 
            curDist = float("inf")
            nextClosest = -1
            for i in range(len(points)): 
                if i not in visited and minDist[i] < curDist: 
                    curDist = minDist[i]
                    nextClosest = i
            
            x1, y1 = points[nextClosest]
            cost += curDist
            visited.add(nextClosest)

            for p in range(len(points)): 
                x2, y2 = points[p]
                dist = abs(x1 - x2) + abs(y1 - y2)
                if dist < minDist[p]: 
                    minDist[p] = dist
        
        return cost