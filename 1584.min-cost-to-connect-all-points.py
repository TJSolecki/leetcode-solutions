import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        costs: dict[tuple[int, int], list[tuple[int, tuple[int, int]]]] = {
            (x[0], x[1]): [] for x in points
        }
        for x1, y1 in points:
            for x2, y2 in points:
                if (x2, y2) != (x1, y1):
                    costs[(x1, y1)].append((abs(x1 - x2) + abs(y1 - y2), (x2, y2)))

        visisted: set[tuple[int, int]] = set()
        frontier: list[tuple[int, tuple[int, int]]] = [
            (0, (points[0][0], points[0][1]))
        ]
        res = 0
        while frontier and len(visisted) != len(points):
            cost, curr = heapq.heappop(frontier)
            if curr in visisted:
                continue
            visisted.add(curr)
            res += cost

            for edge in costs[curr]:
                heapq.heappush(frontier, edge)

        return res
