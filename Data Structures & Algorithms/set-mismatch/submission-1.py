class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < len(nums):
            index = nums[i]-1
            if nums[i] != nums[index]:
                nums[i],nums[index] = nums[index], nums[i]
                continue
            i+=1
        ans = []
        for i,e in enumerate(nums):
            if e-1 != i:
                return [e,i+1]
                break
        
        