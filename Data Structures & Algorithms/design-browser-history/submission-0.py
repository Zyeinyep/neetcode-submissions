class Node:
    def __init__(self, val="",next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
   
    
    def visit(self, url: str) -> None:
        self.home.next = Node(url,None,self.home)
        self.home = self.home.next
    
    def back(self, steps: int) -> str:
        while self.home and self.home.prev and steps > 0:
            self.home = self.home.prev
            steps -=1
        return self.home.val

    def forward(self, steps: int) -> str:
        while self.home and self.home.next and steps >0:
            self.home = self.home.next
            steps -=1
        return self.home.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)