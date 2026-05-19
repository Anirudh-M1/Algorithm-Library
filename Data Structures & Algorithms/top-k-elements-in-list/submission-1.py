class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqArray = [[] for i in range(len(nums)+1)]
        
        for val,cnt in counts.items(): 
            freqArray[cnt].append(val)
        
        ans = []
        for bucket in reversed(freqArray): 
            for val in bucket:
                ans.append(val) 
                if len(ans) == k: 
                    return ans
