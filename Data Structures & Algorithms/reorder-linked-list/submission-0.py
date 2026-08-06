# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p1 = slow.next
        prev = None
        while p1:
            temp = p1.next
            p1.next = prev
            prev = p1
            p1 = temp
        
        slow.next = prev
        fast = head
        left = slow.next
        while fast != slow and left:
            temp = fast.next
            left_temp = left.next
            fast.next = left
            left.next = temp
            left = left_temp
            fast = temp
        slow.next = None
        





        
        