class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            best = max(best,count)
        return best

        