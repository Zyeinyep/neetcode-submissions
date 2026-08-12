from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2 != 0 or sum(nums) %2 != 0:
            return False
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        for k,v in seen.items():
            if v &1:
                return False
        return True        