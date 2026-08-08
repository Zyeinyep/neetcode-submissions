# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0
        prev = None

        while l1 and l2:
            new_val = l1.val+l2.val+carry
            if new_val < 10:
                l1.val = new_val
                carry = 0
            else:
                l1.val = new_val % 10
                carry = new_val // 10
            if l1.next and not l2.next:
                l2.next = ListNode(0)
            elif not l1.next and l2.next:
                l1.next =ListNode(0)
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if carry != 0:
            prev.next = ListNode(carry)
        return head