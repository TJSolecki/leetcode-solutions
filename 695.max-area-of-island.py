class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.max_area = 0
        self.curr_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return

            grid[r][c] = 0
            self.curr_area += 1
            self.max_area = max(self.max_area, self.curr_area)
            if r - 1 >= 0:
                dfs(r - 1, c)
            if r + 1 < rows:
                dfs(r + 1, c)
            if c - 1 >= 0:
                dfs(r, c - 1)
            if c + 1 < cols:
                dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.curr_area = 0
                    dfs(r, c)

        return self.max_area
