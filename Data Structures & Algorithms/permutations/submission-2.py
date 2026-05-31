class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: 
            return [[nums[0]]]
        print(nums)
        arrs = self.permute(nums[1:])
        ans = []
        print(arrs)

        for arr in arrs:
            for i in range(len(arr)+1): 
                arrCpy = arr.copy()
                arrCpy.insert(i, nums[0])
                ans.append(arrCpy)
        
        return ans