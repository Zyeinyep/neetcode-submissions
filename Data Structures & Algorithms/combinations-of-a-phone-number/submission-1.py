class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d= {"2":["a", "b", "c"],
        "3":["d", "e", "f"],"4":["g", "h", "i"],"5":["j", "k", "l"],
        "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"],}
        comb = []
        def backtrack(path,curr):
            if curr == len(digits):
                if path:
                    comb.append("".join(path[:]))
                return
            for j in d[digits[curr]]:
                    path.append(j)
                    backtrack(path,curr+1)
                    path.pop()
            
        backtrack([],0)
       
        return comb
        