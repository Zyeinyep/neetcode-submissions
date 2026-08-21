# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            l = dfs(node1.left,node2.left)
            r = dfs(node1.right, node2.right)
            return l and r
        def match(root1,subRoot1):
            if not root1 or not subRoot1:
                return False
            if root1.val == subRoot1.val:
                if dfs(root1,subRoot1):
                    return True
            if match(root1.left, subRoot1):
                return True
            if match(root1.right, subRoot1):
                return True
            return False

        if match(root,subRoot):
            return True
        return False 





