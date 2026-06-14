class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        seen = {}
        def dfs(i, remaining, numCoins): 
            if (i,remaining, numCoins) in seen:
                return seen[(i, remaining,numCoins)]

            if remaining == 0:
                return numCoins
            
            if (remaining != 0 and i >= len(coins)) or remaining < 0: 
                return float("inf")
            
            
            take = dfs(i, remaining - coins[i], numCoins+1)
    

            skip = dfs(i + 1, remaining, numCoins)

            best = min(take, skip)
            
            seen[(i,remaining,numCoins)] = best
            return best
        
        ans = dfs(0, amount, 0)

        return ans if ans != float("inf") else -1
