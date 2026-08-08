class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        nums.sort()
        def backtrack(path, start, total):
            if total == target:
                comb.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path,i, total+nums[i])
                path.pop()
        backtrack([],0, 0)
        return comb
        