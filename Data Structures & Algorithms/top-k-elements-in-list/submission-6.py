from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for v,f in freq.items():
            heapq.heappush(heap,(f,v))
            if len(heap) > k:
                heapq.heappop(heap)
        l = []
       
        for i,j in heap:
            l.append(j)
        return l
    






        