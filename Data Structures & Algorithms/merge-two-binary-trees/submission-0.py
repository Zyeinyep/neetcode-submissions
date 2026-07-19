# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        def dfs(root1, p1,root2,i):
            if not root1 and not root2:
                return 
            if not root1 and root2:
                newnode = TreeNode(root2.val)
                if i:
                    p1.right = newnode
                else:
                    p1.left = newnode
                dfs(newnode.left, newnode, root2.left,  0)
                dfs(newnode.right, newnode, root2.right,  1)
                return
            if root1 and not root2:
                return
            root1.val += root2.val

            dfs(root1.left, root1, root2.left,  0)
            dfs(root1.right, root1, root2.right,  1)
        dfs(root1, None, root2, 0)
        return root1
        