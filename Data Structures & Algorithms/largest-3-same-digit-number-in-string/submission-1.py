class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        ans = ""
        for r in range(3, len(num) + 1):
            curr = num[l:r]
            print(curr)
            if curr[0] == curr[1] == curr[2]:
                if len(ans) == 0 or int(ans[0]) <= int(curr[0]):
                    ans = curr
                
            l += 1
        return ans





        