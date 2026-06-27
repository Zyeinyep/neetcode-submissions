class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        order = []
        for i in range(len(nums) - 2):
            e = - nums[i]
            left = i +1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s == e:
                    s_orted = sorted([nums[i],nums[left],nums[right]])
                    if s_orted not in order:
                        order.append(s_orted)
                    left += 1
                    right -= 1
                elif s < e:
                    left += 1
                else:
                    right -= 1
        return order       






        