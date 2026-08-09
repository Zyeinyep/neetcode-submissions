class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []

        def backtrack(chess):
            if chess == n:
                ans.append(["".join(row[:]) for row in board])
                return
            for i in range(n):
                if check(board,chess,i):
                    board[chess][i] = "Q"
                    backtrack(chess+1)
                    board[chess][i] = "."

        def check(board,chess,i):
            for row in range(chess):
                if board[row][i] == "Q":
                    return False

            row = chess - 1
            column = i - 1
            while row >= 0 and column >= 0:
                if board[row][column] == "Q":
                    return False
                row -= 1
                column -= 1

   
            row = chess - 1
            column = i + 1

            while row >= 0 and column < n:
                if board[row][column] == "Q":
                    return False
                row -= 1
                column += 1
            return True

            
        backtrack(0)
        return ans 
        