from math import *
from functools import *
class Solution:
    """
    Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

    Example 1:
    Input: n = 3
    Output: 3

    Example 2:
    Input: n = 11
    Output: 0
    Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

    Constraints:
    1 <= n <= 231 - 1

    Related Topics
    Math, Binary Search

    More challenges
    2505. Bitwise OR of All Subsequence Sums
    2576. Find the Maximum Number of Marked Indices
    910. Smallest Range II
    """
    # tc O(logN)
    @staticmethod
    def findNthDigit1(n):
        """there are 9 numbers with 1 digit, 90 numbers with 2 digits, 900 numbers with 3 digits, ..."""
        digit = base = 1 # starting from 1 digit
        while n > 9*base*digit: # upper limit of d digits
            n -= 9*base*digit
            base *= 10
            digit += 1
        q, r = divmod(n-1, digit)
        return int(str(base+q)[r])

print(Solution.findNthDigit1(1000000000))