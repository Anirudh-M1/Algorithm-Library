class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while True:
            s = 0
            print(n)

            if n == 1:
                return True
            
            if n in seen:
                return False

            seen.add(n)

            while n != 0:
                digit = n%10
                n = n//10
                s += digit**2
            n = s

