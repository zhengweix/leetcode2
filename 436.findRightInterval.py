from heapq import *
class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        result = [-1 for i in range(n)]
        eheap, sheap = [], []

        for i, p in enumerate(intervals):
            heappush(sheap, (-p[0], i))
            heappush(eheap, (-p[1], i))

        for i in range(n):
            me, ie = heappop(eheap)
            if -sheap[0][0] >= -me:
                ms, iss = heappop(sheap)
                while sheap and -sheap[0][0] >= -me:
                    ms, iss = heappop(sheap)
                result[ie] = iss
                heappush(sheap, (ms, iss))
        return result