class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def backtrack(path,start):
            subsets.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        backtrack([],0)
        return subsets
        