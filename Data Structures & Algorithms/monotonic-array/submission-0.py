class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        d = None
        prev = None
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                prev = d
                d = nums[i] < nums[i+1]
                if prev != d and prev != None:
                    return False
        return True

        