class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        visited = set()

        def dfs(i): 
            
            if i in visited:
                return 
            
            visited.add(i)

            for a in adj[i]:
                dfs(a)
        count=0

        for i in range(n): 
            if i not in visited: 
                count +=1 
                dfs(i)
        return count 