class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            return [[]]
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