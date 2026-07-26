class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(n):
            if n > len(cost) -1:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = min(cost[n] + dp(n+1), cost[n] + dp(n+2))
            return memo[n]
        ans = min(dp(0), dp(1))
        return ans
        