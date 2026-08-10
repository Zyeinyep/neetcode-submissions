from collections import Counter
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:    
        count = 0
        for w in words:
            count += 1
            for ch in w:
                if ch not in allowed:
                    count -=1
                    break
        return count



        