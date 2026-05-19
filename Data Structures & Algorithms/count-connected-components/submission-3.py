class Solution:
    from collections import deque
    class Node: 
        def __init__(self, val): 
            self.val = val
            self.neighbors = []

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unvisited = set(range(n))

        valToNode = {}
        for e in edges: 
            node1Val = e[0]
            node2Val = e[1]

            if node1Val not in valToNode:
                valToNode[node1Val] = self.Node(node1Val)

            if node2Val not in valToNode:
                valToNode[node2Val] = self.Node(node2Val)
            
            valToNode[node2Val].neighbors.append(node1Val)
            valToNode[node1Val].neighbors.append(node2Val)


        unvisited = list(unvisited)
        visited = set()

        def bfs(nodeVal):
            queue = deque()
            queue.append(nodeVal)
            
            while queue: 
                val = queue.popleft()

                if val in visited: 
                    continue

                visited.add(val)

                print(valToNode[val].neighbors)
                for neighbor in valToNode[val].neighbors: 
                    queue.append(neighbor)

        ccs = 0
        self.left = len(unvisited)
        prevleft = len(unvisited)

        while unvisited:
            node = unvisited[0]
            
            if node in visited: 
                del unvisited[0]
                continue

            ccs +=1 

            if node in valToNode: 
                bfs(node)

            del unvisited[0]

        return ccs






            
