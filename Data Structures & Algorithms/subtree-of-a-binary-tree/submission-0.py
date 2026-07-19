# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return False
            if sametree(root,subRoot):
                return True
            l = dfs(root.left)
            r = dfs(root.right)
            if l == 1 or r == 1:
                return True
            return False

        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            l = sametree(p.left, q.left)
            r = sametree(p.right, q.right)
            if l == 0 or r == 0:
                return False
            return True
        return dfs(root)
            
        