from collections import defaultdict
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = defaultdict(int)
        for i in chars:
            d[i] += 1
        count = 0
        for i in words:
            curr = defaultdict(int)
            count += len(i)
            for j in i:
                curr[j] +=1
            for k,v in curr.items():
                if d[k] < v:
                    count -= len(i)
                    break
        return count

        