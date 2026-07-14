
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        count = 1
        ans = 0
        for e in nums:
            if e-1 not in d:
                count = 1
                while e + count in d:
                    count += 1
                ans = max(ans,count)

        return ans




        