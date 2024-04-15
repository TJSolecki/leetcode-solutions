from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        self.fresh = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        # Add rotten oranges ot queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    self.fresh += 1

        def process(r: int, c: int) -> bool:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return False

            grid[r][c] = 2
            self.fresh -= 1
            q.append((r, c))
            return True

        steps = 0
        while q:
            add_step = False
            for _ in range(len(q)):
                r, c = q.popleft()
                add_step = process(r + 1, c) or add_step
                add_step = process(r - 1, c) or add_step
                add_step = process(r, c + 1) or add_step
                add_step = process(r, c - 1) or add_step
            if add_step:
                steps += 1

        return -1 if self.fresh != 0 else steps
