class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dfs(i, buyInPrice): 
            if (i, buyInPrice) in memo:
                return memo[(i, buyInPrice)]
            if i >= len(prices): 
                return 0

            if buyInPrice  == None:
                #if we dont have anyting to sell yet (1) buy or (2) keep skipping 
                memo[(i, buyInPrice)] = max(dfs(i + 1, prices[i]), dfs(i + 1, None)) 
                return memo[(i, buyInPrice) ]
            
            #sell or keep
            memo[(i, buyInPrice)] = max(dfs(i + 2, None)  + prices[i] - buyInPrice, dfs(i+1, buyInPrice))

            
            return memo[(i, buyInPrice)]

        return max(dfs(0, None), dfs(2, prices[0]))