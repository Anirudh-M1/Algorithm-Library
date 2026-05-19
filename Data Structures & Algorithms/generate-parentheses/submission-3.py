class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(n, subarray, left, right):
            print("***")
            print(subarray)
            print(f"left {left}, right {right}, and n = {n}")

            if left > n:
                return

            if left == n and right == n: 
                res.append(subarray)
                return
            
            dfs(n, subarray + "(", left + 1, right)
            
            if right < left: 
                dfs(n , subarray + ")", left, right + 1)

        dfs(n, "", 0, 0)
        return res
