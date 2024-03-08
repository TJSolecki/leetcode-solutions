class Solution(object):
    def pacificAtlantic(self, matrix: list[list[int]]) -> list[list[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(matrix), len(matrix[0])

        def dfs(visited: set, r: int, c: int, prev: int):
            if (
                (r, c) in visited
                or r < 0
                or c < 0
                or c >= cols
                or r >= rows
                or matrix[r][c] < prev
            ):
                return

            visited.add((r, c))
            height = matrix[r][c]

            dfs(visited, r + 1, c, height)
            dfs(visited, r - 1, c, height)
            dfs(visited, r, c + 1, height)
            dfs(visited, r, c - 1, height)

        for col in range(cols):
            dfs(pacific, 0, col, matrix[0][col])
            dfs(atlantic, rows - 1, col, matrix[rows - 1][col])

        for row in range(rows):
            dfs(pacific, row, 0, matrix[row][0])
            dfs(atlantic, row, cols - 1, matrix[row][cols - 1])

        return list(map(lambda cord: list(cord), atlantic.intersection(pacific)))
