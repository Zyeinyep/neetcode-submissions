class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = 0
        for n in nums:
             ans ^= n
        mask= ans&(-ans)
        a =0 
        b = 0
        for n in nums:
            if n&mask:
                a^=n
            else:
                b^=n
        return [a,b]
        