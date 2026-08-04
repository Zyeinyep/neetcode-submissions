from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = Counter(t)
        d1 = defaultdict(int)
        ans = ""
        curr = []
       
        for r in range(len(s)):
            curr.append(s[r])
            d1[s[r]] += 1
           
            while self.check(d,d1):
              
                if ans == "" or len(ans) > len(curr):
                    ans = curr[:]
                k = curr.pop(0)
             
                d1[k] -=1
                if d1[k] ==0:
                    del d1[k]
            
                
        return "".join(ans)

    def check(self,d,d1):
       
        for k,v in d.items():
            if k not in d1:
                return False
            if v > d1[k]:
                return False
        return True
        
                

        


        