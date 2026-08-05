class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack=[]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
                continue
            a = stack.pop()
            b = stack.pop()
            if i == "+":
                num = a+b
            elif i == "-":
                num=b-a
            elif i == "*":
                num = a*b
            else:
                num=int(b/a)
            stack.append(num)
        return stack.pop()
            


        