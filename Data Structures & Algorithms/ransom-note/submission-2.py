from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26

        
        for e in magazine:
            count[ord(e) - ord("a")] +=1
        
        for e in ransomNote:
            count[ord(e) - ord("a")] -=1
            if count[ord(e) - ord("a")] < 0:
                return False
        return True

        