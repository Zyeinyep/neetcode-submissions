class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) + 3 < len(word2) or len(word1) -3 > len(word2):
            return -1
        memo = {}
        def dp(i,j,n):
            if j < 0:
                return i+1
            if i < 0:
                return j+1
            if (i,j,n) in memo:
                return memo[(i,j,n)]
            if word1[i] == word2[j]:
                memo[(i,j,n)] = dp(i-1,j-1, n) 
            else:
                memo[(i,j,n)] = 1+ min(dp(i,j-1,n-1), dp(i-1,j,n-1),dp(i-1,j-1,n-1))
            return memo[(i,j,n)]
        return dp(len(word1)-1, len(word2)-1, 3)
