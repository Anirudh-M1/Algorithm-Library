# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levelToArray = defaultdict(list[int])
        level = 0
        self.DFS(root, level)
        return (list(self.levelToArray.values()))

    def DFS(self, root, level): 
        if not root:
            return

        self.levelToArray[level].append(root.val)
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)
