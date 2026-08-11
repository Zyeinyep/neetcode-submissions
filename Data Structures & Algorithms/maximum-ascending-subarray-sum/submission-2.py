class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = -float("inf")
        curr = prev = nums[0]
      
        for i in range(1,len(nums)):
            if prev < nums[i]:
                curr += nums[i]
                prev = nums[i]
            else:
                ans = max(curr,ans)
                curr = nums[i]
                prev = nums[i]
        return max(ans,curr)

        