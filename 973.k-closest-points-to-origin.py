import math
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for point in points:
            distance = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)) * -1

            heapq.heappush(heap, (distance, point[0], point[1]))
            if len(heap) > k:
                heapq.heappop(heap)

        return list(map(lambda x: [x[1], x[2]], heap))
