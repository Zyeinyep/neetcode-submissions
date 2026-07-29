class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i =0 
        j = 0
        count = 0
        for j in t:
            if i == len(s):
                return True
            if s[i] == j:
                i+=1
            
        
        if i == len(s):
            return True
        return False
            

        