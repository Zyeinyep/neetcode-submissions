class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(min(word1,word2,key=len))
        merged = ""
        for i in range(l):
            merged += word1[i]
            merged += word2[i]
        merged += word1[l:]
        merged += word2[l:]
        
        return merged
        


