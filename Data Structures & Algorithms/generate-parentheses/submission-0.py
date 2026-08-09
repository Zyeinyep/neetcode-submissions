class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paran = []
        def backtrack(path,opening,closing):
            if opening ==0 and closing ==0 and len(path) == 2*n:
                paran.append("".join(path[:]))
                return
            for i in range(opening):
                path.append("(")
                backtrack(path,opening-i-1, closing)
                path.pop()
            for j in range(closing):
                if opening >= closing:
                    break
                path.append(")")
                backtrack(path,opening, closing-j-1)
                path.pop()

        backtrack([],n,n)
        return paran