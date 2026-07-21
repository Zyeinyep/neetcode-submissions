class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        v = set()
        def dfs(row, column):
            image[row][column] = color
            up = row - 1
            down = row + 1
            left = column - 1
            right = column + 1
            dirs = []
            v.add((row,column))
            
            if up > -1:
                dirs.append((up, column))
            if down < len(image):
                dirs.append((down, column))
            if left > -1:
                dirs.append((row, left))
            if right < len(image[0]):
                dirs.append((row, right))

            for r,col in dirs:
                if (r, col) not in v:
                    if image[r][col] == c:
                        dfs(r,col)
        dfs(sr, sc)
        return image


        