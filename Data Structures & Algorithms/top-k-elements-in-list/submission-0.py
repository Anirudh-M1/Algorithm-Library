class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqArray = [[] for i in range(len(nums)+1)]
        
        for val,cnt in counts.items(): 
            freqArray[cnt].append(val)
        
        ans = []
        for val in reversed(freqArray): 
            for v in val: 
                if k == 0: 
                    break
                ans.append(v)
                k-=1

        return ans