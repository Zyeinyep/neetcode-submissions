class MyQueue:

    def __init__(self):
        self.stack = []
        self.q = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.q.append(self.stack.pop())
        ans = self.stack.pop()
       
        while self.q:
            self.stack.append(self.q.pop())
        return ans

        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()