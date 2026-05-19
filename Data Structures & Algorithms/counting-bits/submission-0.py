class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1): 
            cntZeros = 0
            while i!= 0: 
                cntZeros += i % 2
                i = i//2
                
            ans.append(cntZeros)
        
        return ans