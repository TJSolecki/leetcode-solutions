from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r: int, c: int):
            q = deque()
            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))
            steps = 1
            visited = set()
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if (
                        row >= ROWS
                        or row < 0
                        or col >= COLS
                        or col < 0
                        or (row, col) in visited
                        or grid[row][col] == -1
                    ):
                        continue
                    visited.add((row, col))
                    grid[row][col] = min(grid[row][col], steps)
                    q.append((row + 1, col))
                    q.append((row - 1, col))
                    q.append((row, col + 1))
                    q.append((row, col - 1))
                steps += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)
