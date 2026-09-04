"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dummy = Node()
        d = {}
        def dfs(curr):
            if curr in d:
                return d[curr]
            if not curr:
                return

            new_node = Node(curr.val)
            d[curr] = new_node

            for neighbor in curr.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        return dfs(node)

            
        