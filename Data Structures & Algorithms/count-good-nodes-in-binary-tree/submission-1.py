# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.countGood = 0 
        self.DFS(root,float("-inf"))

        return self.countGood
    def DFS(self, root, maxSoFar): 
        if not root: 
            return

        if root.val>=maxSoFar: 
            self.countGood +=1
            maxSoFar = root.val
        
        self.DFS(root.left, maxSoFar)
        self.DFS(root.right, maxSoFar)
