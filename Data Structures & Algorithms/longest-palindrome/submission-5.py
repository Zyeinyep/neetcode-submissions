from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1

        total = 0
        odd = 0
        for k,v in d.items():
      
            if v % 2 == 0:
                total += v
            else:
                odd = 1
                total += (v//2)*2
        return total + odd


            

        

        