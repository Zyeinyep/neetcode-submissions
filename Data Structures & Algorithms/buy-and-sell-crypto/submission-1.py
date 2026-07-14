class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        cheapest = float("inf")

        for i in prices:
            cheapest = min(cheapest, i)
            curr = i - cheapest
            best = max(best, curr)
        return best

        