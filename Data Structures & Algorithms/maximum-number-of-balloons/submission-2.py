from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        if d['o'] >= 2 and d['l'] >=2:
            return min(d['b'] , d['a'], d['l']//2, d['o']//2, d['n'])
        return 0
        