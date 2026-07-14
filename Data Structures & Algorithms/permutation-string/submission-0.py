from collections import Counter, deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = deque(s2[:len(s1)])
        if Counter(window) == Counter(s1):
            return True


        for e in range(len(s1), len(s2)):
            window.popleft()
            window.append(s2[e])
            if Counter(window) == Counter(s1):
                return True
        return False


            
                



        