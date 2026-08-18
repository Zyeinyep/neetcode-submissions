class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4:
            return False
        parts = [0]*4
        target = sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        def backtrack(start):
            if start == len(matchsticks):
                return True
            for p in range(len(parts)):
                if parts[p] + matchsticks[start] <= target:
                    parts[p] += matchsticks[start]
                    if backtrack(start+1):
                        return True
                    parts[p] -= matchsticks[start]
            return False
        return backtrack(0)
        
                
        