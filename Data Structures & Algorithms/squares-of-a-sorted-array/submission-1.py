class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        negSquared = []
        posSquared = []
        for n in nums: 
            if n < 0: 
                negSquared.append(n**2)
            else:
                posSquared.append(n**2)
        

        idx1, idx2 = 0, 0
        negSquared = negSquared[::-1]
        ans = []
        while idx1 < len(negSquared) and idx2 < len(posSquared):
            if negSquared[idx1] < posSquared[idx2]: 
                ans.append(negSquared[idx1])
                idx1 += 1 
            else:
                ans.append(posSquared[idx2])
                idx2 += 1  


        if idx1 < len(negSquared):
            ans.extend(negSquared[idx1:])
        if idx2 < len(posSquared): 
            ans.extend(posSquared[idx2:])
        
        return ans