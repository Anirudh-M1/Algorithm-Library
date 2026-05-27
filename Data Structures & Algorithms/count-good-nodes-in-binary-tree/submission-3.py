# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # planning. perform dfs, have a max val so far tracker, and count all that are safe, ** max value so far will only increase as we go deeper **
        self.countGood = 0
        def dfs(root,maxValSoFar): 
            if not root:
                return
            
            if root.val >= maxValSoFar:
                self.countGood += 1
                maxValSoFar = root.val
            
            
            dfs(root.left, maxValSoFar)
            dfs(root.right, maxValSoFar)

        dfs(root, root.val)

        return self.countGood