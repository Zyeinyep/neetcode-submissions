"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                return 
         
            for c in node.children:
                dfs(c)
            
            ans.append(node.val)
          
        dfs(root)
        return ans
            
            

        