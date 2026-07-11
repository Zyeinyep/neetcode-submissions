class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(start, path):
            subsets.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i +1, path)
                path.pop()
            

        backtrack(0, [])
        return subsets
        