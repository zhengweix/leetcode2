from collections import *
class Solution:
    '''
    Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
    A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
    The length of a clear path is the number of visited cells of this path.

    Example 1:
    https://assets.leetcode.com/uploads/2021/02/18/example2_1.png
    Input: grid = [[0,1],[1,0]]
    Output: 2

    Example 2:
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4

    Example 3:
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1


    Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1

    Array, Breadth-First Search, Matrix

    turo
    '''
    # Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    # Output: 4
    # tc: O(n), sc: O(n)
    def shortestPathBinaryMatrix(self, grid):
        ans, m, n = 0, len(grid), len(grid[0])
        queue = deque([[0,0]])
        grid[0][0] = 1
        while queue:
            ans += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == n - 1 and y == m - 1:
                    return ans
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        #! careful j and i in grid!
                        if 0 <= i < n and 0 <= j < m and grid[j][i] == 0: # to check cell is valid or not
                            #! careful j and i in grid!
                            grid[j][i] = 1
                            queue.append([i, j])
        return -1

    def main(self):
        print(self.shortestPathBinaryMatrix([[0,0,0],[0,0,0],[0,0,0],[0,0,0]]))

S = Solution()
S.main()
