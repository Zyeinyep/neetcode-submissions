class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(total,start):
            if total == target and start == len(nums):
                return 1
            if start >= len(nums):
                return 0
            if (total, start) in memo:
                return memo[(total, start)]

            memo[(total, start)] = (backtrack(total + nums[start], start + 1) + backtrack(total - nums[start], start + 1))
            return memo[(total, start)]
        return backtrack(0,0)
        