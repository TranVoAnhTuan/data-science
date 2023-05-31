class Solution:
    def solve(self, board) -> None:
        if not board:
            return
        def dfs(i,j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board) or board[i][j] != 'O':
                return
            board[i][j]='S'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)
        for j in range(len(board)):
            dfs(0,j)
            dfs(len(board[0])-1,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
        return board
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve = Solution()
print(solve.solve(board))
