from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        heap = []
        for i in nums:
            d[i] += 1
        
        for key,v in d.items():
            heapq.heappush(heap,(-v,key))
        l = []
        
        z = min(k,len(heap))
        
        for i in range(z):
            l.append(heapq.heappop(heap)[1])
        return l




        