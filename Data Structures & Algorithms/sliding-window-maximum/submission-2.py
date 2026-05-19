from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        windowLeft = 0
        ans = []
        for windowRight, num in enumerate(nums): 
            
            while dq and num > dq[-1][0]:
                dq.pop()     
            dq.append((num, windowRight))

            print(f"dq {dq}")
            print(f"current window {nums[windowLeft:windowRight]}")
            
            if dq[0][1] < windowLeft: 
                    dq.popleft()

            if windowRight - windowLeft + 1 >= k:
                ans.append(dq[0][0])
                windowLeft+=1

        return ans