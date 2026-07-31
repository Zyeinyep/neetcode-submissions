class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        curr = nums[0]
        curr_s = nums[0]
        for i in range(1,len(nums)):
          
            if curr < nums[i]:
                curr = nums[i]
                curr_s += curr
               
               

            else:
                curr= nums[i]
                curr_s = nums[i]
          
            total = max(total, curr_s)
        return total
        