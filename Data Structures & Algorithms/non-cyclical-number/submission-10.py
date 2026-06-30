class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while True: 
            fast = self.nxtVal(self.nxtVal(fast))
            slow = self.nxtVal(slow)
            print(f"f {fast}")
            print(f"s {slow}")
            if fast == 1:
                return True
            if fast == slow:
                return False
        
        return True


    def nxtVal(self, n): 
        s = 0
        while n!=0: 
            d = n %10
            n = n//10

            s += d**2

        return s