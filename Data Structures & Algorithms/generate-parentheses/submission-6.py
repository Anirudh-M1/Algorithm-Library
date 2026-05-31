class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, substring): 
            if left == right == n: 
                res.append(substring)
                return
            
            if left < n:
                dfs(left+ 1, right, substring + "(")
                 
            if right < left:
                dfs(left, right + 1, substring + ")")
                
        
        dfs(0, 0, "")

        return res