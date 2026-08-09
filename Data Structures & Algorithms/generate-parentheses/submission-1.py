class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paran = []
        def backtrack(path,opening,closing):
            if opening ==0 and closing ==0 :
                paran.append("".join(path[:]))
                return
            if opening:
                path.append("(")
                backtrack(path,opening-1, closing)
                path.pop()
            if closing:
                if opening < closing:
                    
                    path.append(")")
                    backtrack(path,opening, closing-1)
                    path.pop()

        backtrack([],n,n)
        return paran