class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            index = nums[i] - 1
            if nums[index] != nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
            else:
                i  +=1
       
        for i,e in enumerate(nums):
            if i+1 != e:
                return e
        return -1
        