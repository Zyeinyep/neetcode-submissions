class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            seen = set()
            for i in r:
                if i == ".":
                    continue
                if i in seen:
                    print("h1")
                    return False
                seen.add(i)

        for c in range(len(board)):
            seen = set()
            for i in range(len(board)):
                if board[i][c] == ".":
                    continue
                if board[i][c] in seen:
                    print("h2")
                    return False
                seen.add(board[i][c])

        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                seen = set()
                for i in range(r, r + 3): 
                    for j in range(c, c + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            print("h3")
                            return False
                        seen.add(board[i][j])
        return True
                        

        