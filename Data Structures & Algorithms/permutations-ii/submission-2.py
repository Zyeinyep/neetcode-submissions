class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        visited = []
        nums.sort()
        def backtrack(path):
            if len(path) == len(nums):
                perm.append(path[:])
                return
            for i,e in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue
                if i not in visited:
                    path.append(e)
                    visited.append(i)
                    backtrack(path)
                    path.pop()
                    visited.pop()
        backtrack([])
        return perm

        