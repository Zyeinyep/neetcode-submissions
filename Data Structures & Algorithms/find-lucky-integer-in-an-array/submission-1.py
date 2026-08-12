from collections import defaultdict
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for i in arr:
            d[i] +=1
        ans = -1
        for k,v in d.items():
            if k == v:
                if ans:
                    ans = max(ans,k)
                else:
                    ans = k
        return ans
