class Solution:
    def isHappy(self, n: int) -> bool:
        self.visited = set()
        self.ans = None
        self.helper(n)
        return self.ans

    def helper(self, num):
        if num == 1:
            self.ans = True
            return
        print(num)
        if num in self.visited: 
            self.ans = False
            return
        self.visited.add(num)
        sumDigs = 0
        digit = 0
        while num != 0:
            digit = num%10
            num = num//10
            sumDigs+= digit *digit

        print(sumDigs)
        self.helper(sumDigs)
        return