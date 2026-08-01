class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for i,e in enumerate(nums):
            if self.prefix:
                self.prefix.append(self.prefix[i-1] + e)
            else:
                self.prefix.append(e)
        

        

    def sumRange(self, left: int, right: int) -> int:
        print(self.prefix)
        if left - 1 > -1:
            return self.prefix[right] - self.prefix[left-1]
    
        return self.prefix[right]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)