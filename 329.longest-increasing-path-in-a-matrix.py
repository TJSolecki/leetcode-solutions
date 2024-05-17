class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = {}

        def dfs(r: int, c: int, prev: int) -> int:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c]),
            )

            return dp[(r, c)]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))

        return res
