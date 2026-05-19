class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            fast = nums[fast] 
            fast = nums[fast]
            slow = nums[slow]
            print(f"fast: {fast}, slow: {slow}")
            if fast == slow: 
                break

        slow = 0
        print("######")
        while fast != slow:
            print(f"fast: {fast}, slow: {slow}")
            fast = nums[fast]
            slow = nums[slow]

        return slow
        
         