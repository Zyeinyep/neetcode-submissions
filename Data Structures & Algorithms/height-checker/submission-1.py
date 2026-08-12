class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0]*101
        for h in heights:
            count[h] +=1
        expected = []
        for i,c in enumerate(count):
            for _ in range(c):
                expected.append(i)
        ans = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                ans += 1
        return ans
        