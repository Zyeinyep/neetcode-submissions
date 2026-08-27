from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(list)
        for i,e in enumerate(s):
            d[e].append(i)

        ans = -1
        for k,v in d.items():
            if len(v) >= 2:
                ans = max(ans, v[-1] - v[0] - 1)
           
        return ans