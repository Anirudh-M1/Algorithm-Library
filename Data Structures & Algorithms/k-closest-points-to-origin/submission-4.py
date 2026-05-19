class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pointsEuc = []
        for x,y in points:
            dist = -(x*x + y*y)
            heapq.heappush(pointsEuc, (dist,(x,y)))
            if len(pointsEuc) > k: 
                heapq.heappop(pointsEuc)

        res = []

        for _, coord in pointsEuc: 
            res.append(list(coord))
        return res
            
        