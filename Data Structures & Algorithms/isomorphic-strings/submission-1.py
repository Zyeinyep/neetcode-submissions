class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        d1 = {}
        for i,e in enumerate(s):
            if e not in d and t[i] not in d1:
                d[e] = t[i]
                d1[t[i]] = e
            else:
                if e in d and d[e] != t[i]:
                        return False
                if t[i] in d1 and d1[t[i]] != e:
                    
                    return False
        return True

        