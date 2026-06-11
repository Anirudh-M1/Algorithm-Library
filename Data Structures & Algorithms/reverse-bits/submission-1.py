class Solution:
    def reverseBits(self, n: int) -> int:
        num = bin(n)[2:]
        ans = []
        for i in num[::-1]: 
           ans.append(i) 

        while len(ans)!= 32:
            ans.append(0)


        return int("".join(map(str,ans)),2)