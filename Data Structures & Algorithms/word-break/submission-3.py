class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            memo = {}
            def dp(i):
                if i < 0:
                    return True
                if i in memo:
                    return memo[i]
            
                for j in range(i+1):
                    if s[j:i+1] in wordDict and dp(j - 1):
                        memo[i] = True
                        return True
                memo[i] = False
                return False

            return dp(len(s) - 1)
        