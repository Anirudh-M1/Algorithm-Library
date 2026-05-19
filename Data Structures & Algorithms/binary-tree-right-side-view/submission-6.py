# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levelToArray = defaultdict(list)
        self.DFS(root, 0)
        ans =[]
        ans = [array[-1] for array in self.levelToArray.values()]
    
        return ans

    def DFS (self, root: Optional[TreeNode], level: int): 
        if not root:
            return
        
        self.levelToArray[level].append(root.val)
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)

        

        



