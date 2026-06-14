class Solution:
    def rob(self, nums: List[int]) -> int:
        #iterative bottom up DP
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1+ n, rob2)

            rob1 = rob2
            rob2 = temp

        return max(rob1,rob2)
            

