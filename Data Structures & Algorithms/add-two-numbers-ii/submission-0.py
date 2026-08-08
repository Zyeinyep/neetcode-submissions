# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy = ListNode(0)
        node = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            new_val = l1_val + l2_val + carry
            dummy.next = ListNode(new_val%10)
            carry = new_val//10
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        node = self.reverse(node.next)
        return node


    def reverse(self,curr):
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev
        return curr
       



        