class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        small = min(coins)
        def dp(n):
            if n == 0:
                return 0
            if n < small:
                return float("inf")
            if n in coins:
                memo[n] = 1
                return 1
            if n in memo:
                return memo[n]
            memo[n] = float("inf")
            for i in coins:
                memo[n] = min(memo[n], dp(n-i) + 1)
            return memo[n]
        ans = dp(amount)
        if ans == float("inf"):
            return -1
        if memo:
            return memo[amount]
        return 0
        