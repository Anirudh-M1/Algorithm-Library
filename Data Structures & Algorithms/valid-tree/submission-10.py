class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # {0: [1, 2, 3], 1:[0, 4], 2:[0], 3: [0], 4: [1]}
        
        adj = defaultdict(list)
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
        

        visited = set()

        def dfs(n, p): 

            if n in visited:
                return False 

            visited.add(n)

            for c in adj[n]:
                if c != p: 
                    if not dfs(c, n): 
                        return False
            
            return True
        
        return dfs(0, None) and len(visited) == n
