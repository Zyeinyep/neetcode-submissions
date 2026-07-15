from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        d = defaultdict(int)
        window = []
        for i,e in enumerate(s):
            window.append(e)
            d[e] += 1
            while sum(d.values()) - max(d.values()) > k:
                removed = window.pop(0)
                d[removed] -= 1
            ans = max(ans,len(window))
        return ans
        

    