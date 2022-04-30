from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mh = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heappush(mh, matrix[i][j])

        nums = nsmallest(k, mh)
        return nums[-1]
