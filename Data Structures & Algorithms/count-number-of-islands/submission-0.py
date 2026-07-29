class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        def dfs(r,c):
            visited.add((r,c))
         
            up = r-1
            down = r+1
            left = c-1
            right = c+1
            d = []
            if up > -1:
                d.append((up,c))
            if down < len(grid):
                d.append((down,c))
            if left > -1:
                d.append((r,left))
            if right < len(grid[0]):
                d.append((r,right))
            for r1,c1 in d:
                if (r1,c1) not in visited and int(grid[r1][c1]) == 1:
                    dfs(r1,c1)

            
        for i, r in enumerate(grid):
            for index, e in enumerate(r):
                
                if int(e) == 1 and ((i,index)) not in visited:
                    dfs(i,index)
                    count += 1
        return count
            