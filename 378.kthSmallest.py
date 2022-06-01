from heapq import *
class Solution:
    '''
    Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order, not the kth distinct element.
    You must find a solution with a memory complexity better than O(n2).

    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

    Input: matrix = [[-5]], k = 1
    Output: -5

    Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -109 <= matrix[i][j] <= 109
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n2

    Follow up:
    Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
    Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for nums in matrix:
            for num in nums:
                heappush(minHeap, num)
        for i in range(k - 1):
            heappop(minHeap)
        return heappop(minHeap)

    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        def helper(mid, row, col):
            i, j, count = row - 1, 0, 0
            while i >= 0 and j < col:
                if matrix[i][j] <= mid:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count

        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = (left + right)//2
            count = helper(mid, n, n)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return right
#373 668 719 786







#373 668 719 786