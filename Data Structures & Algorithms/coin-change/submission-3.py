class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        seen = {}
        def dfs(i, remaining): 
            if (i,remaining) in seen:
                return seen[(i, remaining)]

            if remaining == 0:
                return 0
            
            if (remaining != 0 and i >= len(coins)) or remaining < 0: 
                return float("inf")
            
            
            take = dfs(i, remaining - coins[i]) + 1
    

            skip = dfs(i + 1, remaining) 

            best = min(take, skip)
            
            seen[(i,remaining)] = best
            return best
        
        ans = dfs(0, amount)

        return ans if ans != float("inf") else -1
