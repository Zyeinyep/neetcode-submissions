# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and not head.next:
            return head
        prev = None
        while head and head.next:
            if not prev:
                curr = head.next
                head.next = curr.next
                curr.next = head
                prev = curr
            else:
                curr = head.next
                head.next = curr.next
                curr.next = prev
                prev = curr

        return prev

        