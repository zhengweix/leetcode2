class Solution:
    '''
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.

    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

    Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.

    String, Dynamic Programming

    Next challenges:
    5 516
    '''
    def countSubstrings(self, s):
        n = len(s)
        ans, dp = 0, [[0] * n for _ in range(n)]
        for l in range(n):
            for i in range(n - l):
                j = i + l
                cond = i + 1 <= j - 1
                if s[i] == s[j] and (not cond or dp[i + 1][j - 1] == j - i - 1):
                    dp[i][j] = (dp[i + 1][j - 1] if cond else 0) + (2 if i < j else 1)
                    ans += 1
                else:
                    dp[i][j] = 0
        print(dp)
        return ans

    def main(self):
        print(self.countSubstrings('aaa'))

S = Solution()
S.main()