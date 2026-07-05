import math
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = math.floor(len(nums)/2)
        d = Counter(nums)

        for k,v in d.items():
            if v >= threshold:
                return k


        