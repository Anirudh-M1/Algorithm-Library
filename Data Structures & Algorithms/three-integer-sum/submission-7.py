class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        for idx, num in enumerate(nums): 
            # print("--new base--")
            left,right = 0, len(nums) - 1

            if left == idx :
                left+=1
            if right == idx:
                right-=1

            while left<right: 

                # print(f"left val : {nums[left]}  left idx : {left}")
                # print(f"right val : {nums[right]}  right idx : {right}")
                # print(f"target val : {-num} target idx {idx}")

                currentComb = sorted([nums[left], nums[right], num])
                
                if nums[left] + nums[right] + num == 0 and tuple(currentComb) not in seen:
                    seen.add(tuple(currentComb))
                    # print(f"SET ADDED {currentComb}")
                elif nums[left] + nums[right] + num < 0:
                    left+=1
                else: 
                    right-=1

                if left == idx :
                    left+=1
                if right == idx:
                    right-=1
        return list(seen)