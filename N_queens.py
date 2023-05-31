def solve_n_queens(n):
    solutions = []
    # Generate empty board
    board = [['.' for _ in range(n)] for _ in range(n)]
    # Check if a queen can be placed in given row and column
    def is_valid(row, col):
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
            if row-i >= 0 and col-i >= 0 and board[row-i][col-i] == 'Q':
                return False
            if row-i >= 0 and col+i < n and board[row-i][col+i] == 'Q':
                return False
            if row+i < n and col-i >= 0 and board[row+i][col-i] == 'Q':
                return False
            if row+i < n and col+i < n and board[row+i][col+i] == 'Q':
                return False
        return True

    # Recursive function to try to place queens on the board
    def backtrack(row):
        # Found a solution, add it to the list
        if row == n:
            solutions.append([''.join(row) for row in board])
            return
        # Try placing queen in each column of the current row
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'
    # Start by placing queens in the first row
    backtrack(0)
    return solutions
if __name__ == '__main__':
    n = int(input('nhap n: '))
    for solution in solve_n_queens(n):
        for row in solution:
            print(row)
        print()




class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        def backtrack(i):
            if i == n:
                res.append(list(board))
            for j in range(n):
                if j not in cols and j-i not in diag and j+i not in off_diag:
                    cols.add(j)
                    diag.add(j-i)
                    off_diag.add(j+i)
                    board.append("."*(j)+"Q"+"."*(n-j-1))
                    backtrack(i+1)
                    board.pop()
                    off_diag.remove(j+i)
                    diag.remove(j-i)
                    cols.remove(j)
        res = []
        board = []
        cols = set()
        diag = set()
        off_diag = set()
        backtrack(0)
        return res