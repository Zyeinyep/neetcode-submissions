class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i =0 
        j = 0
        count = 0
        while j < len(s) and i < len(t):
            if t[i] == s[j]:
                count +=1 
                i+=1
                j+=1
                continue
            else:
                i+=1
        
        if count == len(s):
            return True
        return False
            

        