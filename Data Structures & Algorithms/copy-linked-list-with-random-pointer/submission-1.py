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
        newToOld = {}
        oldToNew[None] = None
        newToOld[None] = None
        while oldNode: 
            newNode = Node(oldNode.val)
            
            newToOld[newNode] = oldNode
            oldToNew[oldNode] = newNode
            
            newPrev.next = newNode
            
            oldNode = oldNode.next
            newPrev = newPrev.next
        
        head = curNode = newList.next

        #2) Go over all nodes and set the random pointer 
        while curNode:
            curNode.random = oldToNew[newToOld[curNode].random]
            curNode = curNode.next
        return head
