# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        if root:
            self.DFS(root)
        return (self.maxSum)
    def DFS(self, root):
        if not root:
            return 0

        leftVal = max(0, self.DFS(root.left))
        rightVal = max(0, self.DFS(root.right))

        curSum = leftVal + rightVal + root.val
        self.maxSum = max(self.maxSum, curSum)
        return max(leftVal,rightVal)  + root.val
