class Solution:
    '''
    In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
    A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
    https://assets.leetcode.com/uploads/2018/10/12/knight.png
    Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

    Example 1:
    Input: x = 2, y = 1
    Output: 1
    Explanation: [0, 0] → [2, 1]

    Example 2:
    Input: x = 5, y = 5
    Output: 4
    Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

    Constraints:
    -300 <= x, y <= 300
    0 <= |x| + |y| <= 300

    Breadth-First Search
    '''
    def minKnightMoves(self, x, y):
        x, y = abs(x), abs(y)
        ans, seen, queue = 0, set(), [(0, 0)]
        while queue:
            size = len(queue)
            for _ in range(size):
                x1, y1 = queue.pop(0)
                if x1 == x and y1 == y:
                    return ans
                for dx1, dy1 in [(2,1), (1,2), (-2,1), (-1,2), (-2,-1), (-1,-2),(2,-1),(1,-2)]:
                    if -2 <= x1 + dx1 and -2 <= y1 + dy1 and (x1 + dx1, y1 + dy1) not in seen:
                        queue.append((x1 + dx1, y1 + dy1))
                        seen.add((x1 + dx1, y1 + dy1))
            ans += 1

    def main(self):
        print(self.minKnightMoves(0, 2))

S = Solution()
S.main()
