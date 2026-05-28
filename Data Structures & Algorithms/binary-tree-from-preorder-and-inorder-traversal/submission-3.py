# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        for idx, val in enumerate(inorder): 
            if val == rootVal: 
                leftRightSplit = idx
                break
        #print(f"root is {root.val}, split index is {leftRightSplit}, root.left preorder array is {preorder[1:leftRightSplit+1]}, root.left in order array is  {inorder[0:leftRightSplit]}")

        root.left = self.buildTree(preorder[1:leftRightSplit+1], inorder[0:leftRightSplit])
        root.right = self.buildTree(preorder[leftRightSplit+1:],inorder[leftRightSplit+1:])

        return root