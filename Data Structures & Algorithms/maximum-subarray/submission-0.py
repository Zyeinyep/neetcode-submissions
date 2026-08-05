class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        curr = -float("inf")
        for i in nums:
            
            curr = max(curr+i, i)
       
            ans = max(ans,curr)
        return ans
        