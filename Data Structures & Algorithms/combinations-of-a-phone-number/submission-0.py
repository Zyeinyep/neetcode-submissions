class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        coms = []
        d = {"2": ["a", "b", "c"],"3": ["d", "e", "f"],"4": ["g", "h", "i"],
        "5": ["j", "k", "l"],"6": ["m", "n", "o"],"7": ["p","q", "r", "s"],
        "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"] }
        def backtrack(path,  index):
            if index == len(digits):
                coms.append("".join(path))
                return
            for i in d[digits[index]]:
                path.append(i)
    
                backtrack(path, index + 1)
                path.pop()
        if digits:
            backtrack([],0)
        return coms
        