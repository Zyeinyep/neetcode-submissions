class Node:
    def __init__(self, key=0, value=0, next_node=None):
        self.key = key
        self.val = value
        self.next = next_node

class LRUCache:

    def __init__(self, capacity: int):
        self.node = None
        self.capacity = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        curr = self.node
        prev = None
        while curr:
            if curr.key == key:
                self.reorder(prev,curr)               
                return curr.val
            prev = curr
            curr = curr.next
        return -1
            
    def reorder(self,prev, curr):
        if prev:
            prev.next = curr.next
            curr.next = self.node
            self.node = curr 

    def put(self, key: int, value: int) -> None:
        curr = self.node
        prev = None

      
        while curr:
            if curr.key == key:
                curr.val = value
                self.reorder(prev, curr)
                return

            prev = curr
            curr = curr.next

       
        self.node = Node(key, value, self.node)
        self.size += 1

        
        if self.size > self.capacity:
            self.size -= 1

            curr = self.node
            while curr.next.next:
                curr = curr.next

            curr.next = None