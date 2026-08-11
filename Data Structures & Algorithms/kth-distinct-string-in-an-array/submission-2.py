from collections import defaultdict
import heapq
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)
        for i in arr:
            d[i] +=1
        for key,v in d.items():
            if v==1:
                k-=1
            if k == 0:
                return key
        return ""
        
            



        
        