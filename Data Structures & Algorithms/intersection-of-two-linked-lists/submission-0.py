# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1 = headA
        head2 = headB
        while head1:
            head2 = headB
            while head2:
                if head1 == head2:
                    return head1
                head2 = head2.next
            head1 = head1.next
        return None
        