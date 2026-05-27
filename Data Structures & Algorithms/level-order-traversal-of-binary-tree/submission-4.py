# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)

        def dfs(root, level): 
            if not root:
                return

            self.ans[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        return list(self.ans.values())