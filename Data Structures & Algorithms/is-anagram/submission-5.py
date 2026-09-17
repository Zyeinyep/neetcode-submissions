from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d,d1 = {}, {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0)+1
            d1[t[i]] = d1.get(t[i],0) + 1
        return d == d1