class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s= s.split(" ")
        d = {}
        d1={}
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if s[i] not in d and pattern[i] not in d1:
                d[s[i]] = pattern[i]
                d1[pattern[i]] = s[i]
            else:
                if s[i] not in d or pattern[i] not in d1 or d[s[i]] != pattern[i] or d1[pattern[i]] != s[i]:
                    return False
        return True



        