class Solution:
    from collections import deque
    class Node: 
        def __init__(self, val): 
            self.val = val
            self.neighbors = []

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unvisited = set(range(n))

        print(unvisited)
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

                print(f"current Val {val}")
                visited.add(val)
                print("decrementing left")
                self.left-=1

                print(valToNode[val].neighbors)
                for neighbor in valToNode[val].neighbors: 
                    queue.append(neighbor)

                
        ccs = 0
        self.left = len(unvisited)
        prevleft = len(unvisited)

        while unvisited and self.left:
            print(f"self.left is {self.left} and prevleft is {prevleft}")
            if self.left != prevleft:
                print(f"grouping found of size {prevleft - self.left}")
                ccs+=1
                prevleft = self.left
            print(f"---starting BFS---")
            
            if unvisited[0] not in valToNode: 
                ccs +=1 
            else:
                bfs(unvisited[0])

            print(f"----ending BFS----")
            del unvisited[0]

        if self.left != prevleft:
            ccs+=1
            prevleft = self.left
        return ccs






            
