class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev = [-1]*len(heights)
        next_s = [len(heights)]*len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            
            stack.append(i)

        stack.clear()
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                idx = stack.pop()
                next_s[idx] = i
            
            stack.append(i)
        best = 0
        for i in range(len(prev)):
            curr = (next_s[i] - prev[i] - 1)*heights[i]
            best = max(best,curr)
        return best



        