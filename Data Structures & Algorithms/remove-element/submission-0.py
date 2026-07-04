class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i, e in enumerate(nums):
            if e != val:
                nums[slow] = e
                slow += 1
        return len(nums[:slow])



             
        