class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #buckets

        c = Counter(nums)
        arr = [[] for i in range(len(nums) + 1)]
        for (key,value) in c.items(): 
            arr[value].append(key)

        ans = []
        for freq in range(len(arr)-1, 0, -1): 
            if arr[freq]: 
                ans.extend(arr[freq])
            if len(ans) >= k: 
                return ans[:k]
        return ans