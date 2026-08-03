from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        ans = -1
        for k,v in d.items():
            if k == v:
                ans = max(ans,k)
        return ans

        