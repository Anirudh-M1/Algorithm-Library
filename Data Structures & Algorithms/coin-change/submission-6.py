class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(i, remaining): 
            if (i, remaining) in memo: 
                return memo[(i, remaining)]
            if i == len(coins) and remaining > 0: 
                return float("inf")
            if remaining < 0: 
                return float("inf")
            if remaining == 0: 
                return 0 
            
            memo[(i, remaining)] = min(dfs(i, remaining - coins[i])+ 1,dfs(i+1, remaining))
            return memo[(i, remaining)] 
        
        ans = dfs(0, amount)
        return  ans if ans != float("inf") else -1