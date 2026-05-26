"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Planning:
        #1) Make deep copy of all nodes with next pointers 
        oldNode = head
        newList = newPrev = Node(0)
        oldToNew = {}
        oldToNew[None] = None
        while oldNode: 
            newNode = Node(oldNode.val)
            oldToNew[oldNode] = newNode
            
            newPrev.next = newNode
            
            oldNode = oldNode.next
            newPrev = newPrev.next
        
        start = curNode = newList.next
        oldNode = head
        #2) Go over all nodes and set the random pointer 
        while oldNode:
            curNode.random = oldToNew[oldNode.random]
            curNode = curNode.next
            oldNode = oldNode.next
        return start
