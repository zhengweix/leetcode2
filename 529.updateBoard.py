from itertools import *
class Solution:
    '''
    Let's play the minesweeper game (Wikipedia, online game)!
    You are given an m x n char matrix board representing the game board where:
    'M' represents an unrevealed mine,
    'E' represents an unrevealed empty square,
    'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
    digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
    'X' represents a revealed mine.
    You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

    Return the board after revealing this position according to the following rules:

    If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
    If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    Return the board when no more squares will be revealed.

    Example 1:
    https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png
    Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
    Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

    Example 2:
    https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png
    Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
    Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

    Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 50
    board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
    click.length == 2
    0 <= clickr < m
    0 <= clickc < n
    board[clickr][clickc] is either 'M' or 'E'.

    Array, Depth-First Search, Breadth-First Search, Matrix

    Detonate the Maximum Bombs
    '''
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
        elif board[i][j] == "E":
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                cnt = 0
                for y, x in product(range(i - 1, i + 2), range(j - 1, j + 2)):
                    if 0 <= y < m and 0 <= x < n and (y, x) != (i, j) and board[y][x] == 'M': cnt += 1
                if cnt:
                    board[i][j] = str(cnt)
                else:
                    board[i][j] = "B"
                    for y, x in product(range(i - 1, i + 2), range(j - 1, j + 2)):
                        if 0 <= y < m and 0 <= x < n and (y, x) != (i, j) and board[y][x] == 'E':
                            stack.append((y, x))
        return board

    def main(self):
        print(self.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3,0]))

S = Solution()
S.main()