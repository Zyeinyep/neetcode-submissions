class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        def dp(n):
            if n > len(nums) - 1:
                
                return 0
            if memo[n] != 0:
                return memo[n]
            memo[n] = max(nums[n] +dp(n+2), dp(n+1))
            return memo[n]
        dp(0)
    
        return max(memo)
        
            
        