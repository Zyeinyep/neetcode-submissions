from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d =  defaultdict(int)
        for i in tasks:
            d[i] +=1
        count = 0
        m = 0
        for k,v in d.items():
            m = max(m,v)
        for k,v in d.items():
            if v == m:
                count +=1
        leng = (n+1)*(m-1)
        leng += count
        
        return max(leng,len(tasks))
        

        