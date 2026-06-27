class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,e in enumerate(nums):
            comp = target - e
            if comp in d:
                return [d[comp], i]
            d[e] = i
        return []




        

        