class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #planning: find the highest rate 
        #bananas per hour if this is equal to max number of bananas in any pile, then each pile will be burnt in a single hour
        # this gives us the ablsute maximum rate over which will provide no benifit, at this and any higher rate it will take len(piles) hours
        r = maxRateNeed = max(piles) 
        l = minRateNeeded = 1

        print(l, r)
        minRate = float("inf")
        while l <= r: 
            m = int((l + r)/2)

            hours = 0
            for banan in piles: 
                hours += math.ceil(banan/m)
                print(hours)

            if hours <= h: 
                minRate = min(minRate,m) 
                r = m - 1
            else:
                l = m + 1
        
        return int(minRate)