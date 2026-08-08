# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        k = k % length

        if k == 0:
            return head

       
        node = head
        for _ in range(length - k):
            node = node.next

        mid = node
      
        mid = node
        dummy = curr = ListNode(0)
        if node == head:
            return head
        while node:
            dummy.next = node
            node = node.next
            dummy = dummy.next
        
        while head != mid:
            dummy.next = head
            head = head.next
            dummy = dummy.next
        dummy.next = None
        return curr.next
            
        