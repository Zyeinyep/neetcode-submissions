# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        prev = None
        while p1 and p2:
            if p1.val < p2.val:
                prev = p1
                p1 = p1.next
            else:
                if prev:
                    prev.next = p2
                
                temp = p2.next
                p2.next = p1
                if not prev:
                    list1 = p2
                prev = p2
                p2 = temp
        if p2:
            if prev:
                    prev.next = p2
            else:
                return list2
        return list1
        