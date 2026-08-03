class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        idx = 0

        while idx < n * n:
            i = idx // n
            j = idx % n
            val = grid[i][j]
            correct_row = (val - 1) // n
            correct_col = (val - 1) % n

            if grid[i][j] != grid[correct_row][correct_col]:
                grid[i][j], grid[correct_row][correct_col] = grid[correct_row][correct_col],grid[i][j]
            else:
                idx += 1
        ans = []
        for idx in range(n * n):
            i = idx // n
            j = idx % n
            e = idx+1
            if grid[i][j] != e:
                return [grid[i][j], e]



        