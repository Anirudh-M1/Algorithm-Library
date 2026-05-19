import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        windowLeft = 0
        window = []
        ans = []
        for windowRight in range(len(nums)): 

            heapq.heappush(window, (-nums[windowRight],windowRight))

            if windowRight - windowLeft+1 >= k: 

                #lazy delete
                while window[0][1] < windowLeft: 
                    heapq.heappop(window)
                
                ans.append(-window[0][0])
                windowLeft+=1 
            
        return ans