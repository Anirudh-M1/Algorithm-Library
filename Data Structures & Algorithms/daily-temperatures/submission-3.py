class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        nearestMax = deque()
        ans = len(temperatures) * [0]

        for i in range(len(temperatures)-1, -1, -1): 
            print("///")
            print(f"on num {temperatures[i], i}")
            print(nearestMax)
            while nearestMax and temperatures[i]>=nearestMax[-1][0]: 
                nearestMax.pop()

            ans[i] = nearestMax[-1][1] - i if nearestMax else 0

            nearestMax.append([temperatures[i], i])

        return ans