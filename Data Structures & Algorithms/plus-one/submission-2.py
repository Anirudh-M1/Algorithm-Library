class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1 
        for d in digits[::-1]:

            if d == 9 and carry ==1:
                ans.append(0)
            elif carry == 1:
                ans.append(d + 1)
                carry = 0
            else:
                ans.append(d)
        
        if carry == 1:
            ans.append(1)
            
        return ans[::-1]