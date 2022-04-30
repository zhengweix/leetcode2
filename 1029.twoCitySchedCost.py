from heapq import *
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        aHeap, bHeap = [], []
        aNum, bNum = 0, 0
        total = 0
        for i, c in enumerate(costs):
            if c[0] <= c[1]:
                aNum += 1
                total += c[0]
                heappush(aHeap, (-(c[0] - c[1]), i))
            else:
                bNum += 1
                total += c[1]
                heappush(bHeap, (-(c[1] - c[0]), i))

        if aNum > bNum:
            while aNum > bNum:
                mxDiff, mxInd = heappop(aHeap)
                c = costs[mxInd]
                heappush(bHeap, (-(c[0] - c[1]), mxInd))
                total -= c[0]
                total += c[1]
                aNum -= 1
                bNum += 1
        elif bNum > aNum:
            while bNum > aNum:
                mxDiff, mxInd = heappop(bHeap)
                c = costs[mxInd]
                heappush(aHeap, (-(c[1] - c[0]), mxInd))
                total -= c[1]
                total += c[0]
                bNum -= 1
                aNum += 1
        return total