# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp:
            if temp.val == val:
                if prev:
                    temp = temp.next
                    prev.next = temp
                else:
                    head = head.next
                    temp = head
                continue
            prev = temp
            temp = temp.next
        return head

        