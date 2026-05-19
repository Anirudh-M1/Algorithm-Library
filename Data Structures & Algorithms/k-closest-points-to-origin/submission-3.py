class Solution:
    import heapq
    from collections import defaultdict
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pointsEuc = []
        for point in points:
            x, y = point[0], point[1]
            pointsEuc.append((x**2 + y**2,[x,y]))
        
        heapq.heapify(pointsEuc)

        arr = []
        for i in range(k): 
            pntInfo = heapq.heappop(pointsEuc)
            arr.append(pntInfo[1])

        return arr
            
        

        