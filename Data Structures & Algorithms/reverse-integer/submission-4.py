class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        maxNum = 2**31 - 1
        minNum = -2**31 
        while x:
            digit = int(math.fmod(x, 10))
            print(digit)
            x = int(x/10)

            if res > maxNum // 10 or  (res == maxNum//10 and digit > maxNum % 10): 
                print("Res too big")
                return 0
            if res < minNum // 10 or (res == minNum//10 and digit < minNum % 10):
                print("Res too small")
                return 0
            res = res  * 10 + digit
        return res