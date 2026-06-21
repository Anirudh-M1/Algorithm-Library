class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums: 
            ans.append(n**2)

        return sorted(ans)