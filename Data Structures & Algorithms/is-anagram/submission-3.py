from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        d1 = defaultdict(int)
        for i in s:
            d[i] += 1
        for i in t:
            d1[i] += 1
        return d == d1