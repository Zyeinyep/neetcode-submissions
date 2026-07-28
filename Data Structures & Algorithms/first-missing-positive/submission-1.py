class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            index = nums[i] - 1
            if 1<= nums[i]<=len(nums) and nums[index] != nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
            else:
                i+= 1
        print(nums)
        for i,e in enumerate(nums):
           if e != i + 1: 
                return i + 1
        return len(nums) + 1
      

        