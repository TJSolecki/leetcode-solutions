import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, time in times:
            adj[src].append((time, dst))

        min_time: dict[int, int] = {}
        min_heap: list[tuple[int, int]] = [(0, k)]
        max_time = 0
        while min_heap and len(min_time) != n:
            time, node = heapq.heappop(min_heap)
            if node in min_time:
                continue
            min_time[node] = time
            max_time = max(max_time, time)
            for w2, n2 in adj[node]:
                if n2 not in min_time:
                    heapq.heappush(min_heap, (time + w2, n2))

        if len(min_time) != n:
            return -1

        return max_time
