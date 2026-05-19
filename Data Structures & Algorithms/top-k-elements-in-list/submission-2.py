class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        for num in nums: 
            count[num] = count.get(num, 0) + 1
            print(count)
        
        for key in count.keys(): 
            heapq.heappush(heap, tuple((count[key],key)))
            if len(heap) > k: 
                heapq.heappop(heap)
                
        return [h[1] for h in heap[::-1]]  
