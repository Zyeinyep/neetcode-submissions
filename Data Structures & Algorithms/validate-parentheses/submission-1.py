class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["(", "{", "["]
        closing = {")":"(", "}":"{" , "]":"["}
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != closing[i]:
                        return False
                stack.pop()
                    
        if len(stack) != 0:
            return False
        return True


        