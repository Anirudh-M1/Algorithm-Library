class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ""
        for i in digits: 
            nums+=str(i)
        
        nums = int(nums)
        nums +=1
        ans = []
        while nums: 
            ans.append(nums%10)
            nums = nums//10
        
        return ans[::-1]