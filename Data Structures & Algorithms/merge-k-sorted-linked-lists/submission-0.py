# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        merged = dummy

        for i,l in enumerate(lists):
            if l:
            
                heapq.heappush(heap,(l.val,i,l))
       
        while heap:
            v,i,arr = heapq.heappop(heap)
            merged.next = ListNode(v)
            value = arr.val
            merged = merged.next
            if arr.next:
                heapq.heappush(heap, (arr.next.val, i, arr.next))
        return dummy.next

