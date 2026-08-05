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
                stack.append(a+b)
            elif i == "-":
                stack.append(b-a)
            elif i == "*":
                stack.append(a*b)
            else:
                stack.append(int(b/a))
        return stack.pop()
            


        