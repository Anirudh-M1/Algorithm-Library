class Solution:
    def isHappy(self, n: int) -> bool:
        def nextVal(num): 
            return sum([int(v)*int(v) for v in str(num)])
        
        slow = nextVal(n)
        fast = nextVal(nextVal(n))

        while fast != 1: 
            if slow == fast:
                return False
            slow = nextVal(slow)
            fast = nextVal(nextVal(fast))

        return True
 