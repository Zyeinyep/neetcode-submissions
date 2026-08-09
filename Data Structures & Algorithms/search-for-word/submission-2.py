class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        indices = []
        for i,e in enumerate(board):
            for i1,e1 in enumerate(e):
                if board[i][i1] == word[0]:
                    indices.append((i,i1))
        visited = set()
        def backtrack(r,c,index):
            if index == len(word):
                return True
            
            dirs =[]
            if r-1 > -1:
                dirs.append((r-1,c))
            if r+1 < len(board):
                dirs.append((r+1,c))
            if c-1 >-1:
                dirs.append((r,c-1))
            if c+1 < len(board[0]):
                dirs.append((r,c+1))
            for r1,c1 in dirs:
                if (r1,c1) not in visited and board[r1][c1] == word[index]:
                    visited.add((r1,c1))
                    if backtrack(r1,c1,index+1):
                        return True
                    visited.remove((r1,c1))

            return False


            return
        for r,c in indices:
            if (r,c) not in visited:
                visited.add((r,c))
                if backtrack(r,c,1):
                    return True
                visited.pop()
        return False
        