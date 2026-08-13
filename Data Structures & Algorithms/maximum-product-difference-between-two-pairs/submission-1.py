class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = b= -float("inf")
        c = d= float("inf")
        for i in range(len(nums)):
            if nums[i] > a:
                b = a
                a = nums[i]
            elif nums[i] > b:
                b = nums[i]
            if nums[i] < c:
                d = c
                c = nums[i]
            elif nums[i] < d:
                d = nums[i]
        return (a*b) - (c*d)

        