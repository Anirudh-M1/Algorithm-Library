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
        #node -> newNode
        hashNode = {}
        hashNode[None] = None
        node = head
        dummy = ans = Node(0)

        while node: 
            #Create new node
            cpyNode = Node(node.val)

            #set the previous Nodes next to be cpy
            dummy.next = cpyNode

            #keep hash
            hashNode[node] = cpyNode

            dummy = dummy.next
            #progress in orig list
            node = node.next

        print(f"Hash {hashNode}")
        cpyNode = ans.next
        origNode = head
        
        while cpyNode: 
            cpyNode.random = hashNode[origNode.random]
            cpyNode = cpyNode.next
            origNode = origNode.next
        
        return ans.next



