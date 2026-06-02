class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i < len(nums) -1: 
            count+=1

            if nums[i] + i >= len(nums) -1: 
                break

            furthest = 0
            bestj = 1

            for j in range(1,nums[i]+1):
                if nums[i + j]  +  j > furthest:
                    furthest = nums[i + j]  +  j
                    bestj = j
            
            i = i + bestj
            

        return count

