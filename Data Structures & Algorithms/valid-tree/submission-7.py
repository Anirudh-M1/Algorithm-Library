class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: 
            return True
        
        visited = set()
        adj = defaultdict(list)

        for s,e in edges:
            adj[s].append(e)
            adj[e].append(s)
        

        def dfs(node,parent): 

            if node in visited:
                return False
            
            visited.add(node)

            for a in adj[node]:
                if a != parent: 
                    if not dfs(a, node):
                        return False
            
            return True


        return dfs(0,None) and len(visited) == n