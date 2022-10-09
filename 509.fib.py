from math import *
class Solution:
    '''
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).

    Example 1:
    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    Example 2:
    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    Example 3:
    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

    Constraints:
    0 <= n <= 30

    Math, Dynamic Programming, Recursion, Memoization

    Split Array into Fibonacci Sequence, Length of Longest,Fibonacci Subsequence, Climbing Stairs, N-th Tribonacci Number
    '''
    def fib(self, n):
        '''Dynamic Programming'''
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]

    def fib1(self, n):
        '''Recursion top-down'''
        if n < 2: # boundary condition
            return n
        return self.fib1(n-2) + self.fib1(n-1)

    def fib2(self, n):
        '''Iteration bottom-up'''
        f0, f1 = 0, 1
        for _ in range(n):
            f0, f1 = f1, f0 + f1
        return f0

    # tc: O(1)
    def fib3(self, n):
        '''Formula golden ratio'''
        phi = (1 + sqrt(5)) / 2  # golden ratio
        return round(phi**n/sqrt(5))

    def fib4(self, n):
        '''fast doubling method'''
        def helper(n):
            if n == 0:
                return [0, 1]
            i, j = helper(n >> 1)
            ii, jj = i * (2 * j -i), i*i + j*j
            return [jj, ii+jj] if n&1 else [ii, jj]
        return helper(n)[0]
    def main(self):
        print(self.fib4(3))

S = Solution()
S.main()