from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            heappush(minHeap, n)

        lst = nlargest(k, minHeap)
        return lst[-1]