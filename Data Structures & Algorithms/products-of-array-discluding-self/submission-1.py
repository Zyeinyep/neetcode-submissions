class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [0*n for n in range(len(nums))]
        pre = [0*n for n in range(len(nums))]
       
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
                continue
            pre[i] = pre[i-1]*nums[i-1]
     

        for i in range(len(nums)-1,-1, -1):
            if i == len(nums) - 1:
                post[i] = 1
                continue
            post[i] = post[i+1]*nums[i+1]
       
        for i in range(len(nums)):
            pre[i] = pre[i]*post[i]
       
        return pre
        