
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        q = []
        visited = []
        for i,e in enumerate(board):
            for i2,e2 in enumerate(e):
                if e2 == word[0]:
                    q.append((i,i2))

        def backtrack(r,c,index):
            print(index, len(word))
            if index == len(word):
                return True
            dirs = choices(r,c)
            for i,e in dirs:
                if (i,e) not in visited and board[i][e] == word[index]:
                    visited.append((i,e))
                    if backtrack(i,e,index+1):
                        return True
                    visited.pop()
            return False
            
        def choices(r,c):
            dirs = []
            up = r - 1
            down = r + 1
            left = c - 1
            right = c + 1
            if -1 < up :
                dirs.append((up,c))
            if down < len(board):
                dirs.append((down,c))
            if -1 < left:
                dirs.append((r, left))
            if right < len(board[0]):
                dirs.append((r, right))
            return dirs


        for r,c in q:
            visited.append((r,c))
            if backtrack(r,c,1):
                return True
            visited.pop()
        return False

                
            
        