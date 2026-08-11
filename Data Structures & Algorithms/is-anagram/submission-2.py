from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        for i in s:
            sd[i] += 1
        td = defaultdict(int)
        for i in t:
            td[i] += 1
        return td == sd
        