from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        d = Counter(nums)
        for key,v in d.items():
            heapq.heappush(heap, (v, key))
            while len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for v,key in heap:
            ans.append(key)
        return ans

           


        