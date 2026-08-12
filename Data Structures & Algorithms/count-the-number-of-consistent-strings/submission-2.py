class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s= set(allowed)
        count = 0
        for i in words:
            if set(i) - s == set():
                print(set(i))
                count +=1
        return count

        