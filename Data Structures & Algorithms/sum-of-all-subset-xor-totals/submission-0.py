class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0
        def backtrack(path,start):
            if path:
                xor = 0
                for i in path:
                    xor ^= i
                nonlocal xor_sum
                xor_sum += xor


            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
                
            
        backtrack([],0)

        return xor_sum
        