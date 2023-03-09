from math import inf
from bisect import *
class Solution:
    """
    Given an m x n matrix grid containing an odd number of integers where each row is sorted in non-decreasing order, return the median of the matrix.
    You must solve the problem in less than O(m * n) time complexity.

    Example 1:
    Input: grid = [[1,1,2],[2,3,3],[1,3,4]]
    Output: 2
    Explanation: The elements of the matrix in sorted order are
                 1,1,1,2,2,3,3,3,4. The median is 2.

    Example 2:
    Input: grid = [[1,1,3,3,4]]
    Output: 3
    Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The
                 median is 3.

    Constraints:
    * m == grid.length
    * n == grid[i].length
    * 1 <= m, n <= 500
    * m and n are both odd.
    * 1 <= grid[i][j] <= 10^6
    * grid[i] is sorted in non-decreasing order.
    """
    @staticmethod
    def matrixMedian(grid):
        def helper(nums1):
            pos, num = 0, nums1[0]
            for i, x in enumerate(nums1):
                if x < num:
                    pos = i
                    num = x
            return pos

        m, n = len(grid), len(grid[0])
        idx = [0] * m
        nums = [row[0] for row in grid]
        lst = []
        for i in range(m*n):
            p = helper(nums)
            lst.append(nums[p])
            idx[p] += 1
            if idx[p] >= n:
                nums[p] = inf
            else:
                nums[p] = grid[p][idx[p]]
        mid = len(lst)//2
        return lst[mid] if len(lst)%2 else (lst[mid]+lst[mid-1])/2

    @staticmethod
    def matrixMedian1(grid):
        m, n = len(grid), len(grid[0])
        lo, hi = inf, -inf
        for row in grid:
            lo = min(lo, row[0])
            hi = max(hi, row[-1])
        while lo < hi:
            mid = lo + hi >> 1
            more = sum(n - bisect_right(row, mid) for row in grid)
            if more > m * n / 2:
                lo = mid + 1
            else:
                hi = mid
        return lo

print(Solution.matrixMedian1([[1,1,2],[2,3,3],[1,3,4]]))