class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        d = {")":"(", "}":"{", "]":"["}
        so = []
        for i in s:
            if i in opening:
                so.append(i)
            else:
                if len(so) == 0:
                    return False
                curr = so.pop()
                if curr != d[i]:
                    return False
        if len(so) != 0:
            return False
        return True

        