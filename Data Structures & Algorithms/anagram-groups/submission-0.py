from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            curr = str(sorted(s))
            d[curr].append(s)
        
        return list(d.values())
            
    





        