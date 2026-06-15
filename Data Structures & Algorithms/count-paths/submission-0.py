class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        path = set()
        visited = {}
        def dfs(i, j):
            if (i,j) in visited: 
                return visited[i,j]
            if not 0 <= i < m or not 0 <= j < n or (i,j) in path: 
                return 0
            if i == m - 1 and j == n - 1: 
                return 1
            
            path.add((i,j))
            ways = (dfs(i + 1, j)
            + dfs(i, j + 1))
            path.remove((i,j))

            visited[(i,j)] = ways

            return visited[(i,j)]
        
        return dfs(0, 0)
            