class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                l = i + 1
                r = len(nums) - 1

                while l < r: 
                    s = nums[l] + nums[r] + nums[i] 
                    if s < 0: 
                        l+=1
                    elif s > 0:
                        r-=1
                    else:
                        if tuple([nums[i], nums[l], nums[r]]) not in ans:
                            ans.add(tuple([nums[i], nums[l], nums[r]]))
                        l +=1
                        r -=1

        return list(ans)

             