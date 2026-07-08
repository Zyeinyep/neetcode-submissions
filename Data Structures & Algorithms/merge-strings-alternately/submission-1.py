class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(min(word1,word2,key=len))
        merged = []
        for i in range(l):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.extend(word1[l:])
        merged.extend(word2[l:])
        
        return "".join(merged)
        


