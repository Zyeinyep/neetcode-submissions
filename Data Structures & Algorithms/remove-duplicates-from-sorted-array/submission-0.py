class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
      
        for f in range(1,len(nums)):
            if nums[f] != nums[s]:
                s += 1
                nums[s] = nums[f]
              
        return len(nums[:s+1])


        