class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_v = 0
        while left < right:
            curr = min(heights[left], heights[right]) * (right-left)
            max_v = max(max_v, curr)
            if heights[left] > heights[right]:
                right -= 1
            else:
               left += 1
        return max_v
            
        
        