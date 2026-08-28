# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node,prev):
            nonlocal ans
            if not node:
                return

            if prev <= node.val:
                ans += 1

            if node.left:
                dfs(node.left, max(prev,node.val))
            if node.right:
                dfs(node.right, max(prev,node.val))
            return
        dfs(root, -float("inf"))
        return ans



        