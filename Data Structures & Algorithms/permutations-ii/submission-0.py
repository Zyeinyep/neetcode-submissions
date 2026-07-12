class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        visited = []
        def backtrack(path):
            if len(path) == len(nums) and path not in perm:
                perm.append(path[:])
                return
            for i,e in enumerate(nums):
                
                if i not in visited:
                    path.append(e)
                    visited.append(i)
                    backtrack(path)
                    path.pop()
                    visited.pop()
        backtrack([])
        return perm

        