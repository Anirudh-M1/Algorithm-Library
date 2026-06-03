class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = [gas[i]-cost[i] for i in range(len(gas))]
        if sum(ans) < 0: 
            return -1 
        total = 0
        res = 0 
        for i, v in enumerate(ans): 
            total += v 

            if total < 0:
                total = 0
                res = i + 1

        
        return res