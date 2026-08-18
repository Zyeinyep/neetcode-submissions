class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        seen = set()
        b = 1
        while len(seen) < len(nums):

            if i not in seen:
                if b:
                    val = nums[i]
                temp = nums[(k+i)%len(nums)]
                nums[(i+k)%len(nums)] = val
                val = temp
                seen.add(i)
                i = (i+k)%len(nums)
                b = 0
            else:
                i = 0
                while i in seen:
                    i += 1
                b = 1
        