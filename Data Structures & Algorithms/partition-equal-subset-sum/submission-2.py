class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total//2
        dp = {0}
        for num in nums:
            next_dp = set(dp)
            for s in dp:
                next_dp.add(s+num)
            dp = next_dp
        return target in dp
        
        