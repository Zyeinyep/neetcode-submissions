class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = [0]*len(nums)
        perm= []

        def backtrack(path,arr):
            print(path)
            if len(path) == len(nums):
                perm.append(path[:])
                return
            for i,e in enumerate(nums):
                if arr[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and arr[i-1] == 0:
                    continue
                arr[i]=1
                path.append(nums[i])
                backtrack(path,arr)
                path.pop()
                arr[i]=0
                   

        backtrack([],arr)
        return perm
        
        