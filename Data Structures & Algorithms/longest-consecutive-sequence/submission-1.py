
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set()
        ans = 0
        nums.sort()
        count = 1
        for e in nums:
            if e-1 in d:
                if e not in d:
                 count+=1
            else:
                count = 1
            d.add(e)
            ans = max(count, ans)
        return ans

        




        