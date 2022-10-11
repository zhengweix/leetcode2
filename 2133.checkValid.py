class Solution:
    '''
    An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
    Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

    Example 1:
    https://assets.leetcode.com/uploads/2021/12/21/example1drawio.png
    Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
    Output: true
    Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
    Hence, we return true.

    Example 2:
    https://assets.leetcode.com/uploads/2021/12/21/example2drawio.png
    Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
    Output: false
    Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
    Hence, we return false.

    Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 100
    1 <= matrix[i][j] <= n

    Array, Hash Table, Matrix
    '''
    def checkValid(self, matrix):
        n, seen = len(matrix), set()
        for y in range(n):
            for x in range(n):
                cand = {(str(matrix[y][x]), y), (x, str(matrix[y][x]))}
                if seen & cand:
                    return False
                seen |= cand
        return True

    def checkValid1(self, matrix):
        return all(len(set(x)) == len(matrix) for x in matrix + list(zip(*matrix)))

    def main(self):
        print(self.checkValid1([[1,2,3],[3,1,2],[2,3,1]]))

S = Solution()
S.main()