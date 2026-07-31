from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        for key,v in d.items():
            if v == 1:
                k-=1
            if  k == 0:
                return key
        return ""

        