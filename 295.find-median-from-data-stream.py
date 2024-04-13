import heapq


class MedianFinder:

    def __init__(self):
        self.small: list[int] = []
        self.large: list[int] = []

    def addNum(self, num: int) -> None:
        if not self.small or -self.small[0] >= num:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) - len(self.large) > 1:
            temp = -heapq.heappop(self.small)
            heapq.heappush(self.large, temp)
        elif len(self.large) - len(self.small) > 1:
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small, -temp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
