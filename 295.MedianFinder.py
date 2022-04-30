from heapq import *
from statistics import *
class MedianFinder:
    def __init__(self):
        self.snums = []
        self.lnums = []

    def addNum(self, num: int) -> None:
        if not self.snums or -self.snums[0] >= num:
            heappush(self.snums, -num)
        else:
            heappush(self.lnums, num)

        m = len(self.snums)
        n = len(self.lnums)
        if m > n + 1:
            heappush(self.lnums, -heappop(self.snums))
        elif m < n:
            heappush(self.snums, -heappop(self.lnums))

    def findMedian(self) -> float:
        if len(self.snums) == len(self.lnums):
            return (-self.snums[0] + self.lnums[0]) / 2.0

        return -self.snums[0] / 1.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

