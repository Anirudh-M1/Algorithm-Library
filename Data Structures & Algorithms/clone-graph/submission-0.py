"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        def dfs(root): 
            if root == None: 
                return
            
            rootCpy = Node(root.val)
            hashmap[root] = rootCpy

            for n in root.neighbors:
                if n not in hashmap:
                    rootCpy.neighbors.append(dfs(n))
                else: 
                    rootCpy.neighbors.append(hashmap[n])
            return hashmap[root]
        
        return  dfs(node)










    