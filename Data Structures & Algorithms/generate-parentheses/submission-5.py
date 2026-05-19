class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n, subarray, left, right):
            
            if left == n and right == n: 
                res.append(subarray)
                return
            
            if left<n:
                dfs(n, subarray + "(", left + 1, right)
            
            if right < left: 
                dfs(n , subarray + ")", left, right + 1)

        dfs(n, "", 0, 0)
        return res
