from functools import cache
class Solution:
    '''
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

    Constraints:
    1 <= n <= 45

    Math, Dynamic Programming, Memoization

    Min Cost Climbing Stairs, N-th Tribonacci Number, Minimum Rounds to Complete All Tasks, Count Number of Ways to Place Houses, Number of Ways to Reach a Position After Exactly k Steps
    '''
    @cache
    def climbStairs(self, n: int) -> int:
        def helper(n):
            return 1 if n < 2 else helper(n - 2) + helper(n - 1)
        return helper(n)

    def climbStairs1(self, n):
        n0, n1 = 1, 1
        for i in range(n-1):
            n0, n1 = n1, n0 + n1
        return n1

    #* golden ratio
    def climbStairs2(self, n):
        phi = (1 + sqrt(5)) / 2
        return round((phi ** (n + 1) - (1 - phi) ** (n + 1)) / sqrt(5))

    def climbStairs3(self, n):
        dp = [0 for i in range(n+2)]
        dp[0], dp[1] = 0, 1
        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n+1]
    def main(self):
        print(self.climbStairs3(5))

S = Solution()
S.main()