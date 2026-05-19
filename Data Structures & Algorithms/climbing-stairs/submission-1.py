class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.ways(n)

    def ways(self, n): 
        if n in self.memo: 
            return self.memo[n]
        if n < 0: 
            return 0 
        if n == 0:
            return 1

        self.memo[n] = self.ways(n-1) + self.ways(n-2)
        return self.memo[n]