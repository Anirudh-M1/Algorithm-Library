class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+ 1): 
            cnt = 0
            while i: 
                i, b = divmod(i, 2)
                if b: 
                    cnt += 1

            ans.append(cnt)
        
        return ans 