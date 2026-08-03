class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        count = 0
        for i,e in enumerate(heights):
            if e != exp[i]:
                count += 1
        return count

        