from collections import defaultdict
from heapq import *
class Solution:
    def topKFrequent(self, nums, k):
        dict = defaultdict(int)
        for n in nums:
            dict[n] += 1

        minHeap = []
        for num, frg in dict.items():
            heappush(minHeap, (frg, num))
            if len(minHeap) > k:
                heappop(minHeap)

        lst = []
        while minHeap:
            lst.append(heappop(minHeap)[1])
        return lst
