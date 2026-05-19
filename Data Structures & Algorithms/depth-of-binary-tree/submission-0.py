# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = 0 if not root.left else self.maxDepth(root.left)
        rightDepth = 0 if not root.right  else self.maxDepth(root.right)

        return max(leftDepth,rightDepth) + 1  
