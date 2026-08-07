"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dummy = node = Node(0,None,None)
        d = {}
        while curr:
            temp = Node(curr.val,None, None)
            dummy.next = temp
            d[curr] = temp
            curr = curr.next
            dummy = dummy.next
        node = node.next
        dummy = node
        while head:
            if head.random:
                node.random = d[head.random]
            head = head.next
            node = node.next
        return dummy



        