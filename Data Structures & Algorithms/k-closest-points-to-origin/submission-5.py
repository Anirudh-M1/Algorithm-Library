class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[-(point[0]**2  + point[1]**2), [point[0], point[1]]] for point in points]
        print(f" x is {-(points[0][0]^2)} y is : {points[0][1]^2} total is {-(points[0][0]^2  + points[0][1]^2)}")
        heapq.heapify(dists)
        print(dists)
        while len(dists) > k:
            heapq.heappop(dists)
        
        return [point for dist, point in dists]
        