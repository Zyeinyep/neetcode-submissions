class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.node = Node()
      
    def get(self, index: int) -> int:
        curr = self.node
        while index > -1 and curr:
           
            curr= curr.next
            
            index-=1
        if curr:
            return curr.val
        return -1

        
        

    def addAtHead(self, val: int) -> None:
        curr = self.node
        n = curr.next
        curr.next = Node(val, n)
        

    def addAtTail(self, val: int) -> None:
        curr = self.node
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val,None)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.node
        while index > 0:
            curr = curr.next
            index -= 1
        temp = curr.next
        curr.next = Node(val,temp)

        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.node
        while index > 0:
            curr = curr.next
            index -=1
        if curr.next:
            temp = curr.next.next
        else:
            temp = None
        curr.next = temp
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)