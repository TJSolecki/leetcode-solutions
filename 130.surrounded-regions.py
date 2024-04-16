class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs_fill(r: int, c: int):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "X":
                return
            board[r][c] = "X"
            dfs_fill(r + 1, c)
            dfs_fill(r - 1, c)
            dfs_fill(r, c + 1)
            dfs_fill(r, c - 1)

        def is_surrounded(r: int, c: int) -> bool:
            if (r, c) in visited:
                return True
            if r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1:
                return False

            visited.add((r, c))
            res = True
            if board[r + 1][c] == "O":
                res = res and is_surrounded(r + 1, c)
            if board[r - 1][c] == "O":
                res = res and is_surrounded(r - 1, c)
            if board[r][c + 1] == "O":
                res = res and is_surrounded(r, c + 1)
            if board[r][c - 1] == "O":
                res = res and is_surrounded(r, c - 1)

            return res

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                visited = set()
                if board[r][c] == "O" and is_surrounded(r, c):
                    dfs_fill(r, c)
