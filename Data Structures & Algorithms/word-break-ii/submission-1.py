class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sent = []
        path = []
        def backtrack(start):
            if start == len(s):
                sent.append(" ".join(path[:]))
                return
            for i in range(start, len(s)):
                curr = s[start:i+1]
                if curr in wordDict:
                    path.append(curr)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return sent


        