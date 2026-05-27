# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #max height is left height + right height of each node and build and compare        
        if not root:
            return 0
        
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        depth= self.depthOfBinaryTree(root.left) + self.depthOfBinaryTree(root.right)
                
        self.maxHeight = max(depth, leftDiameter+rightDiameter)

        return self.maxHeight

    def depthOfBinaryTree(self, root) -> int: 
        if not root:
            return 0
        
        return 1 + max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right))

