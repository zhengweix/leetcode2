class Solution:
    '''
    You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
    https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png
    Return true if the square is white, and false if the square is black.
    The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

    Example 1:
    Input: coordinates = "a1"
    Output: false
    Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

    Example 2:
    Input: coordinates = "h3"
    Output: true
    Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

    Example 3:
    Input: coordinates = "c7"
    Output: false

    Constraints:
    coordinates.length == 2
    'a' <= coordinates[0] <= 'h'
    '1' <= coordinates[1] <= '8'

    Math String

    Escape The Ghosts, Similar String Groups, Maximum Score From Removing Stones
    '''
    def squareIsWhite(self, coordinates):
        return (ord('a') + ord(coordinates[0]) + 1 + int(coordinates[1]))%2 != 0

    def squareIsWhite1(self, coordinates):
        return (ord(coordinates[0]) - 97) & 1 == int(coordinates[1]) & 1

    def main(self):
        print(self.squareIsWhite1('c3'))

S = Solution()
S.main()