import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if len(stones) == 1 else 0
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        def helper():
            if len(stones) <= 1:
                return stones[0] * -1 if len(stones) == 1 else 0
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            if x != y:
                heapq.heappush(stones, -1 * (y - x))
            return helper()

        return helper()
