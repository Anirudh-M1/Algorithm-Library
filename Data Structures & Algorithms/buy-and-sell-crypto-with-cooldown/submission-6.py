class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i, holding): 
            if(i, holding) in memo: 
                return memo[(i,holding)] 
            if i >= len( prices): 
                return 0
            
            if not holding: 
                # buy
                buy = dfs(i + 1, True) - prices[i]
                #skip
                skip = dfs(i + 1, False)
                memo[(i, holding)] = max(buy, skip) 
                return memo[(i, holding)] 
            else: 
                #sell
                sell = dfs(i + 2, False) + prices[i]
                #hold
                hold = dfs(i + 1, True)
                memo[(i, holding)] = max(sell, hold)

                return memo[(i, holding)] 
            
        
        return dfs(0, False)