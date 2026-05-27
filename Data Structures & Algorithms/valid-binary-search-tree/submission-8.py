# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        def dfs(root, left, right): 
            if not root:
                return
            
            if root.val <= left or root.val >= right: 
                print(f"setting valid to false {root.val, left, right}")
                self.isValid = False
                return
            
            dfs(root.left, left, root.val)
            dfs(root.right, root.val, right)          



        dfs(root, float("-inf"), float("inf"))

        return self.isValid