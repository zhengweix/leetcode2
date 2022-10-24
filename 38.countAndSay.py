from itertools import *
class Solution:
    '''
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
    To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
    For example, the saying and conversion for digit string "3322251":
    https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg
    Given a positive integer n, return the nth term of the count-and-say sequence.

    Example 1:
    Input: n = 1
    Output: "1"
    Explanation: This is the base case.

    Example 2:
    Input: n = 4
    Output: "1211"
    Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = say "1" = one 1 = "11"
    countAndSay(3) = say "11" = two 1's = "21"
    countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

    Constraints:
    1 <= n <= 30

    String

    Encode and Decode Strings
    String Compression
    '''
    @staticmethod
    def countAndSay(n):
        def helper(s):
            return ''.join(str(len(list(g))) + k for k, g in groupby(s))
        dp = ['1'] # base condition
        for i in range(1, n): # 2, 3, 4
            dp.append(helper(dp[i-1]))
        return dp[n-1]

    @staticmethod
    def countAndSay1(n):
        if n == 1:
            return '1'
        return ''.join(str(len(list(g))) + k for k, g in groupby(Solution.countAndSay1(n-1)))

print(Solution.countAndSay1(5))