class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n, subarray, left, right):
            print("***")
            print(subarray)
            print(f"left {left}, right {right}, and n = {n}")

            if left - right < 0 or n < 0:
                return
            if n == 0 and left == right: 
                res.append(subarray)
                return
            
            subarray += ("(")
            dfs(n - 1, subarray, left + 1, right)
            
            subarray = subarray[:-1]
            subarray += (")")
            dfs(n - 1, subarray, left, right + 1)

        dfs(2* n, "", 0, 0)
        return res
