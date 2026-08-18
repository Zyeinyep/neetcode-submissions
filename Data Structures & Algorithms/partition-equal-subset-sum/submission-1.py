class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        nums.sort(reverse=True)
        parts = [0]*2
        def backtrack(start):
            if start == len(nums):
                return True
            for i in range(2):
                if parts[i] + nums[start]  <= s:
                    parts[i] += nums[start]
                    if backtrack(start+1):
                        return True
                    parts[i] -= nums[start]
                if parts[i] == 0:
                    break
            return False

        s = sum(nums) // 2
        return backtrack(0)
        
        