class Solution:
    '''
    Given an m x n matrix, return all elements of the matrix in spiral order.

    Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

    Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

    Array, Matrix, Simulation

    Spiral Matrix II, Spiral Matrix III, Spiral Matrix IV
    '''
    def spiralOrder(self, matrix):
        ans, m, n = [], len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        for _ in range(n * m):
            ans.append(matrix[y][x])
            matrix[y][x] = False
            if m <= y+dy or y+dy < 0 or n <= x+dx or x+dx < 0 or not matrix[y + dy][x + dx]:
                dx, dy = -dy, dx
            x += dx
            y += dy
        return ans

    def main(self):
            print(self.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

S = Solution()
S.main()