class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted([(sp, p) for sp, p in zip(speed,position)], key = lambda x:x[1], reverse = True)
        print(fleets)

        stack = []
        for s, p in fleets: 
            stack.append((target - p)/s)
            if len(stack) >=2 and stack[-2] >= stack[-1]: 
                stack.pop()
        
        return len(stack)

