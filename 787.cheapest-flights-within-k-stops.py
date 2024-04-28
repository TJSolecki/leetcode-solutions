class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices[:]
            for frm, to, cost in flights:
                if prices[frm] != float("inf") and prices[frm] + cost < temp[to]:
                    temp[to] = prices[frm] + cost
            prices = temp

        return -1 if prices[dst] == float("inf") else int(prices[dst])
