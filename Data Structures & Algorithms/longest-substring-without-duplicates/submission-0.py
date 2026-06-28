class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        max_l = 0
        arr = []
        for f in range(len(s)):
            arr.append(s[f])
            while self.check(arr):
                print(arr)
                arr.pop(0)
                print(arr)
                slow += 1

            max_l = max(max_l, len(arr))
        return max_l
    def check(self, arr):
        seen = []
        for i in arr:
            if i in seen:
                return True
            seen.append(i)
        return False


        