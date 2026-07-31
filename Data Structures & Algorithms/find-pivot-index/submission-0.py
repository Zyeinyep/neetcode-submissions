class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        prev = 0
        for i, e in enumerate(nums):
            r -= e
            l += prev
            if l == r:
                return i
            prev = e
        return -1
        
        