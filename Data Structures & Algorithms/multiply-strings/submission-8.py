class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0]* (len(num1) + len(num2))

        if num1 =="0" or num2 == "0": 
            return "0"
        

        for i in range(len(num2) - 1, -1, -1): 
            for j in range(len(num1) -1, -1, -1): 
                mult = int(num2[i]) * int(num1[j])
                ans[i + j + 1] += mult
                ans[i + j] += ans[i + j + 1]//10
                ans[i + j + 1] %= 10

        if ans[0] == 0:
            return "".join(map(str, ans[1:]))
        else: 
            return "".join(map(str, ans))

