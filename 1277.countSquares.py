import numpy
class Solution:
    '''
    Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

    Example 1:
    Input: matrix =
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    Output: 15
    Explanation:
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.

    Example 2:
    Input: matrix =
    [
      [1,0,1],
      [1,1,0],
      [1,1,0]
    ]
    Output: 7
    Explanation:
    There are 6 squares of side 1.
    There is 1 square of side 2.
    Total number of squares = 6 + 1 = 7.

    Constraints:
    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1

    Array, Dynamic Programming, Matrix

    Minimum Cost Homecoming of a Robot in a Grid, Count Fertile Pyramids in a Land
    '''
    def countSquares(self, matrix):
        ans = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                # check squares side > 1
                if y > 0 and x > 0 and matrix[y][x]:
                    # increment at [m-1,n-1] equals value at [m-1,n-1], and x squares expanded from [m-1, n-1], 0 <= x <min(m, n)
                    matrix[y][x] = min(matrix[y - 1][x], matrix[y - 1][x - 1], matrix[y][x - 1]) + 1
                ans += matrix[y][x]
        print(matrix)
        return ans

    def main(self):
        print(self.countSquares([[0,1,1,1], [1,1,1,1], [0,1,1,0]]))

S = Solution()
S.main()