class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [False] * len(nums)
        end= len(nums) -1 
        for i in range(len(nums) - 1, -1, -1): 
            if nums[i]>= end - i: 
                ans[i] = True  
                end = i
        
        print(ans)


        return ans[0]