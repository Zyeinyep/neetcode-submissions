class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        curr = [nums[0]]
        for i in range(1,len(nums)):
            if curr[-1] < nums[i]:
                curr.append(nums[i])
            else:
                curr.clear()
                curr.append(nums[i])
            total = max(total, sum(curr))
        return total
        