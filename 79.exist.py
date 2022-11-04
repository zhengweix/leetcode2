from collections import *
class Solution:
    '''
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Example 1:
    https://assets.leetcode.com/uploads/2020/11/04/word2.jpg
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

    Example 2:
    https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

    Example 3:
    https://assets.leetcode.com/uploads/2020/10/15/word3.jpg
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false


    Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

    Array, Backtracking, Matrix

    Word Search II

    turo
    '''
    def exist(self, board, word):
        if Counter(word) - Counter(sum(board, [])):
            return False

        m, n = len(board), len(board[0])
        def helper (i, j, k):
            if board[i][j] == word[k]:
                #! careful length is n-1
                if k == len(word) - 1:
                    return True
                temp = board[i][j]
                board[i][j] = '' # mark as visited
                for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                    if 0 <= x < m and 0 <= y < n and board[x][y] and helper(x, y, k + 1):
                        return True
                board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if helper(i, j, 0):
                    return True
        return False

    def main(self):
        print(self.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

S = Solution()
S.main()