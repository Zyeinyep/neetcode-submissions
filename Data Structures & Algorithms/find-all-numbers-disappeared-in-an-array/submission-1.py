class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[correct],nums[i] = nums[i], nums[correct]
                continue
            i+=1
        ans = []
        for i,e in enumerate(nums):
            if e != i+1:
                ans.append(i+1)
        return ans

