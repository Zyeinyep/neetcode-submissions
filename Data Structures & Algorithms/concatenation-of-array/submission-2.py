class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        j = 0
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans
        