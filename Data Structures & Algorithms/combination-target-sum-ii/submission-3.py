class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        candidates.sort()
        def backtrack(path, remaining, start):
            if remaining == 0:
                comb.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(path, remaining-candidates[i], i+1)
                path.pop()
        backtrack([],target, 0)
        return comb

        