from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = defaultdict(int)
        m = defaultdict(int)
        for e in ransomNote:
            r[e] +=1
        
        for e in magazine:
            m[e] +=1
        
        for k,v in r.items():
            if m[k] < v:
                return False
        return True

        