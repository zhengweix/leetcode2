import numpy
class Solution:
    '''
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the board must contain the digits 1-9 without repetition.
    Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.


    Example 1:
    https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
    Input: board =
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

    Example 2:
    Input: board =
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

    Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

    Array, Hash Table, Matrix

    Sudoku Solver, Check if Every Row and Column Contains All Numbers

    verkada
    '''
    # tc: n^2
    def isValidSudoku(self, board):
        def helper(lst):
            lst = list(filter(lambda x: x.isdigit(), lst))
            return len(set(lst)) == len(lst)

        n, board = len(board), numpy.array(board)
        return all([helper(board[y:y + 3, x:x + 3].flatten()) for y in range(0, n, 3) for x in range(0, n, 3)]) and all([helper(board[y]) for y in range(n)]) and all([helper(board[:, x]) for x in range(n)])

    def isValidSudoku1(self, board):
        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cand = {(i, board[i][j]), (board[i][j], j), (i // 3, j // 3, board[i][j])}
                    if seen & cand:
                        return False
                    seen |= cand
        return True

    def main(self):
        print(self.isValidSudoku1([["8","3",".",".","7",".",".",".","."],
                                   ["6",".",".","1","9","5",".",".","."],
                                   [".","9","8",".",".",".",".","6","."],
                                   ["8",".",".",".","6",".",".",".","3"],
                                   ["4",".",".","8",".","3",".",".","1"],
                                   ["7",".",".",".","2",".",".",".","6"],
                                   [".","6",".",".",".",".","2","8","."],
                                   [".",".",".","4","1","9",".",".","5"],
                                   [".",".",".",".","8",".",".","7","9"]]))

S = Solution()
S.main()