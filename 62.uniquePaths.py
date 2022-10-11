class Solution:
    '''
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 109.

    Example 1:
    https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png
    Input: m = 3, n = 7
    Output: 28

    Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

    Constraints:
    1 <= m, n <= 100

    Related Topics
    Math， Dynamic Programming， Combinatorics

    Next Challenges:
    Unique Paths II， Minimum Path Sum， Dungeon Game， Minimum Path Cost in a Grid， Minimum Cost Homecoming of a Robot in a Grid， Number of Ways to Reach a Position After Exactly k Steps

    turo
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for x in range(n)] for y in range(m)]
        for x in range(n):
            dp[0][x] = 1
        for y in range(1, m):
            for x in range(n):
                dp[y][x] = dp[y][x-1] + dp[y-1][x]

        return dp[m-1][n-1]

    def main(self):
        print(self.uniquePaths(1, 2))
S = Solution()
S.main()