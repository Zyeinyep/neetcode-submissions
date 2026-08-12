from collections import defaultdict
import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d =  defaultdict(int)
        for i in nums:
            d[i] += 1
        ans = 0
        for k,v in d.items():
            if v > 1:
                comb = math.factorial(v)/(2*(math.factorial(v-2)))
                ans += int(comb)
        return ans

        