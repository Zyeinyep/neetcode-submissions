# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        p = None
        while slow:
            temp = slow.next
            slow.next = p
            p = slow
            slow = temp
        prev.next = p
        
        slow = prev.next
        mid = slow
        ans = 0 
        while head != mid:
            ans = max(ans, head.val + slow.val)
            slow = slow.next
            head = head.next
            
        return ans



        


        