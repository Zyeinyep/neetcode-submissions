class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = len(min(strs, key=len))
        prefix = ""

        
        for i in range(num):
            curr = strs[0][i]
            for s in strs:
                if s[i] != curr:
                    return prefix
            prefix += curr
        return prefix

        