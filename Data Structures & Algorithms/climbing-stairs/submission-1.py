class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(state):
            if state == 1:
                memo[1] = 1
                return 1
            if state == 2:
                memo[2] = 2
                return 2
            if state in memo:
                return memo[state]
            result = dp(state - 1) + dp(state - 2)
            memo[state] = result
            return result
   
        return dp(n)
        
        

        