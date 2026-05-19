class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valToLongest = {}
        nums.sort()
        for num in nums: 
            valToLongest[num] = max(valToLongest.get(num, 0), valToLongest.get(num-1, 0)+1)

        if valToLongest: 
            return max(valToLongest.values())
        else: return 0