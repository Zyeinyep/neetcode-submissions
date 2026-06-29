from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        subarray = []
        ans = 0
        for f in range(len(s)):
            subarray.append(s[f])
            while self.check(subarray,k) :
                
               
                subarray.pop(0)
                slow += 1
            ans = max(ans, len(subarray))
            
        return ans

    def check(self, arr,k):
        d = Counter(arr)
        r = max(d,key=d.get)
        
        if len(arr) - int(d[r]) > k:
            return True
        return False



        