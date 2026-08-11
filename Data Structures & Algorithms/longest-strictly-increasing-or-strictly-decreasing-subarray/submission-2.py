class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in nums:
            if stack:
                if stack[-1] == i:
                    res = max(res,len(stack))
                    stack.clear()
                    stack.append(i)
                    continue
                if len(stack) >= 2:
                    if stack[-2] > stack[-1]:
                        if stack[-1] < i:
                            res = max(res,len(stack))
                            temp = stack[-1]
                            stack.clear()
                            stack.append(temp)
                            stack.append(i)
                            continue
                    else:
                        if stack[-1] > i:
                            res = max(res,len(stack))
                            temp = stack[-1]
                            stack.clear()
                            stack.append(temp)
                            stack.append(i)
                            continue
                
            stack.append(i)
        return max(len(stack),res)
           
            

        