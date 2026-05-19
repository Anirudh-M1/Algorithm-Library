class Solution:
    from collections import deque
    class Node: 
        def __init__(self, val): 
            self.val = val
            self.neighbors = []

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        queue = deque()
        if n == 1:
            return len(edges) == 0
            
        queue.append((self.createGraph(edges), None))
        visited = set()
        while queue: 
            (node, prev) = queue.popleft()
            print(node.val)
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in node.neighbors:
                if prev is not None: 
                    prevVal = prev.val
                else: 
                    prevVal = None

                if neighbor != prev:
                    queue.append((neighbor, node))
        
        return len(edges) == n - 1 and len(visited) == n


            
    def createGraph(self, edges): 
        valToNode = {}
        for edge in edges: 
            node1Val = edge[0]
            node2Val = edge[1]
        
            if node1Val not in valToNode: 
                valToNode[node1Val] = self.Node(node1Val)
            if node2Val not in valToNode: 
                valToNode[node2Val] = self.Node(node2Val)
            
            valToNode[node1Val].neighbors.append(valToNode[node2Val])
            valToNode[node2Val].neighbors.append(valToNode[node1Val])

        return valToNode[edges[0][0]]