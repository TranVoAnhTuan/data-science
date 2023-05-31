class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)

        def backtrack(row: int, count: int) -> int:
            if row == n:
                return count + 1
            else:
                for col in range(n):
                    if cols[col] or diag1[row + col] or diag2[row - col + n -1]:
                        continue
                    cols[col], diag1[row + col], diag2[row - col + n -1] = True, True, True
                    count = backtrack(row + 1, count)
                    cols[col], diag1[row + col], diag2[row - col + n -1] = False, False, False
                return count
        return backtrack(0,0)
if __name__ == '__main__':
    n = int(input())
    res = Solution()
    print(res.totalNQueens(n))