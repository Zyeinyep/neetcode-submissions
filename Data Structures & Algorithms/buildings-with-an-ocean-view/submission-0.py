class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [-1]*len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                idx = stack.pop()
                res[idx] = i
            stack.append(i)
        ans = []
        for i,e in enumerate(res):
            if e == -1:
                ans.append(i)
        return ans
        