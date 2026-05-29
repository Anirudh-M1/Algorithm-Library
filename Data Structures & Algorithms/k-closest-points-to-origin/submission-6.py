class Solution:
    #O(k) space but O(nlog(k)) time
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(ans, (-dist, point))
            
            if len(ans) > k: 
                heapq.heappop(ans)

        return [point for _, point in ans]