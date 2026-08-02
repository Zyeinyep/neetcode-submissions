class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i+= 1
        ans = []
        for i,e in enumerate(nums):
            if i + 1 != e:
                ans.append(i+1)
        return ans
        