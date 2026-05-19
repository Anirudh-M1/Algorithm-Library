class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.heap = [-i for i in nums]
        self.k = k

        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        heapCpy = list(self.heap)

        print(self.k)
        print(self.heap)
        for i in range(self.k): 
            ans = heapq.heappop(heapCpy)

        return -ans
       
