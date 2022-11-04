class Solution:
    '''
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.

    Example 1:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.

    Example 2:
    Input: text1 = "abc", text2 = "abc"
    Output: 3
    Explanation: The longest common subsequence is "abc" and its length is 3.

    Example 3:
    Input: text1 = "abc", text2 = "def"
    Output: 0
    Explanation: There is no such common subsequence, so the result is 0.

    Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.

    String, Dynamic Programming

    Longest Palindromic Subsequence,
    Delete Operation for Two Strings,
    Shortest Common Supersequence,
    Maximize Number of Subsequences in a String
    '''
    @staticmethod
    def longestCommonSubsequence(text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n+1)]
        for y in range(1, n+1):
            for x in range(1, m+1):
                if text2[y-1] == text1[x-1]:
                    dp[y][x] = dp[y-1][x-1]+1
                else:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
        return dp[n][m]

    @staticmethod
    def longestCommonSubsequence1(text1, text2):
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in reversed(range(m)):
            prev = 0
            for j in reversed(range(n)):
                curr = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = curr
        return dp[0]

print(Solution.longestCommonSubsequence1("bsbininm", "jmjkbkjkv"))

