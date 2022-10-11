from itertools import *
class Solution:
    '''
    On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.
    When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.
    Return the number of available captures for the white rook.

    Example 1:
    https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG
    Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: In this example, the rook is attacking all the pawns.

    Example 2:
    https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG
    Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 0
    Explanation: The bishops are blocking the rook from attacking any of the pawns.

    Example 3:
    https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG
    Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    Output: 3
    Explanation: The rook is attacking the pawns at positions b5, d6, and f5.

    Constraints:
    board.length == 8
    board[i].length == 8
    board[i][j] is either 'R', '.', 'B', or 'p'
    There is exactly one cell with board[i][j] == 'R'

    Array, Matrix, Simulation

    Count Unguarded Cells in the Grid
    '''
    def numRookCaptures(self, board):
        n = len(board)
        for y, x in product(range(n), range(n)):
            if board[y][x] == "R":
                break

        def helper(dx, dy):
            x1, y1 = x, y
            while 0 <= x1 < n and 0 <= y1 < n:
                if board[y1][x1] not in ('p', 'B'):
                    x1 += dx
                    y1 += dy
                else:
                    return board[y1][x1] == 'p'
            return False

        ans = 0
        for dir in ((1,0), (0,1), (-1,0), (0,-1)):
            ans += helper(*dir)
        return ans


