class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i,e in enumerate(nums):
            target = -e
            arr = nums[i+1:]
            left = 0
            right = len(arr) - 1
            while left < right:
                summed = arr[left] + arr[right]
                if summed == target:
                    s = sorted([e, arr[left], arr[right]])
                    if s not in ans:
                        ans.append(s)
                    left += 1
                    right -= 1
                elif summed < target:
                    left += 1
                else:
                    right -= 1
        return ans

        