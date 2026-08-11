class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        l1 = 0 
        count = 0
        while l < len(s) and l1 < len(t):
            if s[l] == t[l1]:
                count +=1
                l+=1
                l1+=1
                continue
            l1+=1
        return count == len(s)
            
        