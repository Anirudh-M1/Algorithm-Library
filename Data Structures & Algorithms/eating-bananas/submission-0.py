class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        left, right = 1,m 
        minSpeed = float("inf")
        while left<=right: 
            mid = (left+right)//2
            totalTime = 0
            for pile in piles: 
                totalTime += math.ceil(float(pile)/mid)
            
            if totalTime <= h: 
                minSpeed = min(mid, minSpeed)
                right = mid-1
            else:
                left = mid+1
            
        return minSpeed