from collections import Counter
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:    
        s = set(allowed)
        count = 0
        for w in words:
            ch = set(w)
            if len(ch - s) == 0:
                count += 1
        return count



        