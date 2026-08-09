class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        if sum(matchsticks) % 4 != 0 or matchsticks[-1] > sum(matchsticks) // 4:
            return False
        visited = [0]*len(matchsticks)
        

        def backtrack(remaining, n):
            if remaining == 0:
                remaining = sum(matchsticks)//4
                n -= 1
                if n == 0:
                    return True
                return backtrack(remaining,n)
              

            for i in range(len(matchsticks)):
                if visited[i] != 1:
                    if matchsticks[i] > remaining:
                        break
                    visited[i] = 1
                    if backtrack(remaining-matchsticks[i],n):
                        return True
                    visited[i] = 0
            return False

        return backtrack(sum(matchsticks)//4 ,4)