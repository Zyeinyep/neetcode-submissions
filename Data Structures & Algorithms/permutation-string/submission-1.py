from collections import defaultdict, Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        curr = defaultdict(int)
        d = Counter(s1)
        window = list(s2[:len(s1)])
       
        for e in window:
            curr[e] += 1

        if curr == d:
            return True

        for i in range(len(s1), len(s2)):
            s = window.pop(0)
            window.append(s2[i])
            curr[s] -= 1
            curr[s2[i]] += 1
            if curr[s] == 0:
                del curr[s]

            if curr == d:
                return True

        return False

        

        