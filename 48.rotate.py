class Solution:
    '''
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

    Example 1:
    https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    Example 2:
    https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


    Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

    Array, Math, Matrix

    Determine Whether Matrix Can Be Obtained By Rotation
    '''
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate1(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[~i] = matrix[~i], matrix[i]

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate2(self, matrix):
        # [::-1] - makes a shallow copy of the original list in reverse order.
        # '*' - makes each sublist in the original list a separate argument to zip()
        # zip() - takes one item from each argument and makes a list/tuple from those, and repeats until all the sublists are exhausted.
        matrix[:] = list(zip(*reversed(matrix)))
        print(matrix)

    def main(self):
        self.rotate2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

S = Solution()
S.main()