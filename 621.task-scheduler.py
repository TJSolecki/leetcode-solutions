import heapq
from typing import Deque
from collections import Counter
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = dict(Counter(tasks))
        time = 1
        max_heap = [-x for x in task_counts.values()]
        heapq.heapify(max_heap)
        queue: Deque[tuple[int, int]] = deque()
        while max_heap or queue:
            time += 1
            if not max_heap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count != 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
