class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = {}
        for w in wordDict:
            d[w] = 1

        segments = []
        def backtrack(path,start):
            if start == len(s):
                segments.append(" ".join(path[:]))
                return
            for i in range(start,len(s)):
                curr_word = s[start:i+1]
                if curr_word in d:
                    path.append(curr_word)
                    backtrack(path,i+1)
                    path.pop()


        backtrack([],0)
        return segments

        