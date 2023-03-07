class Solution:
    """
    Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
    Return the maximum product you can get.
    Example 1:
    Input: n = 2
    Output: 1
    Explanation: 2 = 1 + 1, 1 × 1 = 1.

    Example 2:
    Input: n = 10
    Output: 36
    Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

    Constraints:
    2 <= n <= 58
    """
    @staticmethod
    def integerBreak(n):
        """Math"""
        if n == 2:
            return 1
        if n == 3:
            return 2

        ans = 1
        while n > 4:
            n -= 3
            ans *= 3
        return ans*n

    @staticmethod
    def integerBreak1(n):
        """top-down DP"""
        ans = [None, 1] + [0] * (n - 1)
        for k in range(2, n+1):
            for i in range(1, k//2 + 1):
                ans[k] = max(ans[k], max(i, ans[i])*max(k-i, ans[k-i]))
        return ans[-1]

    @staticmethod
    def integerBreak2(n):
        """top-down DP"""
        ans = [None, 1] + [0] * (n - 1)
        for k in range(2, n + 1):
            for i in range(1, k // 2 + 1):
                ans[k] = max(ans[k], max(i, ans[i]) * max(k - i, ans[k - i]))
        return ans[-1]

print(Solution.integerBreak1(10))