from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = defaultdict(int)
        for i in words[0]:
            d[i] += 1

        ans = []
        for k,v in d.items(): 
            eq = 1   
            for i in range(1,len(words)):
                curr = defaultdict(int)
                for e in words[i]:
                    curr[e]+=1
                if not curr[k]:
                    eq=0
                    break
                else:
                    v = min(v,curr[k])
            if eq == 1:
                for j in range(v):
                    ans.append(k)
        return ans
                
