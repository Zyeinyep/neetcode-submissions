class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
       
        for i, e in enumerate(prices):
            
            if i ==  0:
                continue
            curr_p = e - min(prices[:i])
            max_p = max(curr_p, max_p)
        return max_p

