from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(list)
        for i,e in enumerate(s):
            d[e].append(i)
        
        for k,v in d.items():
            if len(v) == 1:
                return v[0]
        return -1
            