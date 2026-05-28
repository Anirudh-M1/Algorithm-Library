class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negStones = [-s for s in stones]
        heapq.heapify(negStones)

        while negStones: 
            if len(negStones) == 1: 
                return -heapq.heappop(negStones)
            s1 = -heapq.heappop(negStones)
            s2 = -heapq.heappop(negStones)
            if s1 - s2:
                heapq.heappush(negStones, -(s1 - s2))

        return 0