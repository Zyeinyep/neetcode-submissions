from collections import deque
class MyStack:

    def __init__(self):
        self.front = deque([])
        self.back = deque([])
        

    def push(self, x: int) -> None:
        self.back.append(x)
        
        

    def pop(self) -> int:
    
        for i in range(len(self.back)-1):
            self.back.append(self.back.popleft())
            
        return self.back.popleft()
        

    def top(self) -> int:
        ans = 0
        for i in range(len(self.back)):
            ans = self.back.popleft()
            self.back.append(ans) 
        return ans
        

    def empty(self) -> bool:
        if not self.back:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()