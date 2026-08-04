class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        topk = []
        freq = defaultdict(int)
        for n in nums:
            freq[n] +=1

        for n,f in freq.items():
            if len(topk) == k:
                if f > topk[0][0]:
                    heapq.heappop(topk)
                    heapq.heappush(topk, (f, n))
            else: 
                heapq.heappush(topk,(f,n))
        
        return [n for f,n in topk]