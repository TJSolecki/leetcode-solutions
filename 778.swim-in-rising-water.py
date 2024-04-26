import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N = len(grid)
        min_time = {}
        min_heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        while min_heap:
            t, x, y = heapq.heappop(min_heap)
            if (x, y) == (N - 1, N - 1):
                return t
            if (x, y) in min_time:
                continue
            min_time[(x, y)] = t
            for x2, y2 in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
                if (x2, y2) in min_time or x2 < 0 or y2 < 0 or x2 >= N or y2 >= N:
                    continue

                heapq.heappush(min_heap, (max(grid[x2][y2], t), x2, y2))

        return -1
