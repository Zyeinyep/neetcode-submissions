# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
    
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        dummy = node = ListNode(0)
        carry = 0
        while stack1 or stack2 or carry:
            if stack1:
                val1 = stack1.pop()
            else:
                val1 = 0

            if stack2:
                val2 = stack2.pop()
            else:
                val2 = 0
            new_val = val1 + val2 + carry
            carry = new_val//10
            dummy.next =ListNode(new_val%10)
            dummy = dummy.next
        
        prev = None
        node = node.next
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev


        

        
         
       



        