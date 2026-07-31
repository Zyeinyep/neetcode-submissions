class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        inc = []
        dec = []
        for i in nums:
            if inc:
                if inc[-1] < i:
                    inc.append(i)
                else:
                    ans = max(ans,len(inc))
                    inc.clear()
                    inc.append(i)
            else:
                inc.append(i)
            if dec:
                if dec[-1] > i:
                    dec.append(i)
                else:
                    ans = max(ans,len(dec))
                    dec.clear()
                    dec.append(i)
            else:
                dec.append(i)
        return max(ans,len(dec), len(inc))


            


        