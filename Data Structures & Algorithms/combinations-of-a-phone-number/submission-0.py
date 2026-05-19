class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        charToDigit = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
                    }
        print(charToDigit[3])
        def dfs(i, curString): 
            if len(curString) == len(digits): 
                res.append(curString)
                return 
            
            for c in charToDigit[int(digits[i])]: 
                dfs(i+1, curString + c)
        
        if digits:
            dfs(0, "")
        
        return res