from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        d = Counter(s)
        even = float("inf")
        odd = 0
        for k,v in d.items():
            if v % 2 == 0:
                even = min(even,v)
            else:
                odd = max(odd,v)
        print(odd, even)
        return odd - even
        