class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = [0]* len(prices)
        for i in range(len(prices) - 1, -1, -1): 
            while stack and prices[i] >= stack[-1]: 
                stack.pop()

            if stack: 
                ans[i] = stack[0] - prices[i]
            
            stack.append(prices[i])

        return max(ans)
            