class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        ans = {}
        def dfs(i,amount): 
            if (i,amount) in ans:
                return ans[(i,amount)]
            if amount < 0: 
                return 0 
            if amount == 0: 
                return 1
            
            if amount != 0 and i >= len(coins):
                return 0 
            
            ways = 0
            ways += dfs(i, amount-coins[i])
            ways += dfs(i+1, amount)
            ans[(i,amount)] = ways
            return ways 

        return dfs(0, amount)