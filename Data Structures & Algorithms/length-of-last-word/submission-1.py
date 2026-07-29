class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while i > -1:
            if s[i] == " ":
                if count == 0:
                    i -= 1
                    continue
                else:
                    break
            count += 1
            i-= 1 


        return count

        