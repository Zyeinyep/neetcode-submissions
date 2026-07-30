class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i in words:
            for j in words:
                if i ==j:
                    continue
                if i in j:
                    ans.add(i)
        return list(ans)


