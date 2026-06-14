class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCoins = [float("inf")]* (amount+ 1)

        minCoins[0] = 0

        for subAmount in range(1, amount+1): 
            for c in coins: 
                if subAmount >=c: 
                    minCoins[subAmount] = min(minCoins[subAmount], minCoins[subAmount -c] + 1)

        
        return minCoins[amount] if minCoins[amount] != float("inf") else -1
