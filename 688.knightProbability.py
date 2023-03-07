from functools import *
class Solution:
    '''
    On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
    A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
    Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
    The knight continues moving until it has made exactly k moves or has moved off the chessboard.
    Return the probability that the knight remains on the board after it has stopped moving.

    Example 1:
    https://assets.leetcode.com/uploads/2018/10/12/knight.png
    Input: n = 3, k = 2, row = 0, column = 0
    Output: 0.06250
    Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
    From each of those positions, there are also two moves that will keep the knight on the board.
    The total probability the knight stays on the board is 0.0625.

    Example 2:
    Input: n = 1, k = 0, row = 0, column = 0
    Output: 1.00000

    Constraints:
    1 <= n <= 25
    0 <= k <= 100
    0 <= row, column <= n - 1

    Dynamic Programming
    
    More challenges
    576. Out of Boundary Paths
    '''
    @staticmethod
    def knightProbability(n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def helper(k1, i, j):
            """Return probability in chessboard at (i, j) with k moves left."""
            if not (0 <= i < n and 0 <= j < n):
                return 0
            if k1 == 0:
                return 1
            return sum(helper(k1-1, i+ii, j+jj) for ii, jj in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)))/8
        return helper(k, row, column)

print(Solution.knightProbability(3, 2, 0, 0))