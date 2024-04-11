class Solution:
    def is_safe(self, row: int, col: int) -> bool:
        for queen_row, queen_col in self.queen_locations:
            if row == queen_row:
                return False
            if col == queen_col:
                return False
            # check diagonal
            if abs(row - queen_row) == abs(col - queen_col):
                return False
        return True

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.board: list[list[str]] = [["." for _ in range(n)] for _ in range(n)]
        self.queen_locations = set()
        res: list[list[str]] = []

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in self.board])
                return
            for col in range(n):
                if self.is_safe(row, col):
                    self.board[row][col] = "Q"
                    self.queen_locations.add((row, col))
                    backtrack(row + 1)
                    self.board[row][col] = "."
                    self.queen_locations.remove((row, col))

        backtrack(0)
        return res
