class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def find(grid):
            for i1, row in enumerate(grid):
                for i,e in enumerate(row):
                    if e == 1:
                        return (i1,i)
        param = 0
        visited = set()
        def dfs(start):
            nonlocal param 
            param += 4
            directions = []
            visited.add((start[0],start[1]))
            if start[0] - 1 > -1:
                directions.append((start[0] - 1, start[1]))
            if start[0] + 1 < len(grid):
                directions.append((start[0] + 1, start[1]))
            if start[1] - 1 > -1:
                directions.append((start[0], start[1] - 1))
            if start[1] + 1 < len(grid[0]):
                directions.append((start[0], start[1] + 1))
            for r,c in directions:
                if grid[r][c] == 1:
                    param -= 1
                    if (r,c) not in visited:
                        dfs((r,c))
                        
                
        start = find(grid)
        dfs(start)
        return param