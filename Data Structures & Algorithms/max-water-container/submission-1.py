class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0 
        left = 0
        right = len(heights) - 1

        while left < right:
            bar = min(heights[left], heights[right])
            curr = bar*(right-left)
            ans = max(ans,curr)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1

        return ans
        

        