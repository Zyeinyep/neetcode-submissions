class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tab = [float("inf")]*(amount+1)
        tab[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    tab[i] = min(tab[i], tab[i-coin] +1)
        if tab[amount] == float("inf"):
            return -1
        return tab[amount]
        