class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        sides = [0]*k
        nums.sort(reverse=True)

        def backtrack(start):
            if start == len(nums):
                return True
            for i in range(k):
                if sides[i] + nums[start] <= sum(nums)// k:
                    sides[i] += nums[start]
                    if backtrack(start+1):
                        return True
                    sides[i] -= nums[start]
                if sides[i] == 0:
                    break

            return False

        return backtrack(0)


        