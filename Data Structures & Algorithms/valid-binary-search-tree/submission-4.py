# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.bst = True 
        self.DFS(root, float("-inf"), float("inf"))

        return self.bst 

    def DFS(self, root, minVal, maxVal): 
        if not root: 
            return
        if root.val<=minVal or root.val>=maxVal:
            self.bst = False
            return 
        self.DFS(root.left, minVal, root.val)
        self.DFS(root.right, root.val, maxVal)


