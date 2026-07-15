
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = nums[:k]
        m = max(window)
        ans = [m]
        for i in range(k, len(nums)):
            s = window.pop(0)
            window.append(nums[i])
            if s == m:
                m = max(window)
            else:
                m = max(m, nums[i])
            ans.append(m)
        return ans

        
        