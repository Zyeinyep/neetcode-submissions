# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:
                return 1
            if not node1 and node2:
                return 0
            if not node2 and node1:
                return 0
            if node1.val != node2.val:
                return 0
            r = dfs(node1.right, node2.right)
            l=dfs(node1.left, node2.left)
        
            return l and r
        if  dfs(p,q) == 1:
            return True
        return False
            

        